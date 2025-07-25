from fastapi import FastAPI, Form, UploadFile, File
from app.utils import serialize_mongo_document
from app.schema import StudentInput
from app.db import students_collection
from app.model import predict_top_3_careers
from app.llm_resume_parser import parse_resume_text
import pandas as pd
import numpy as np
import fitz  # PyMuPDF

#chatbot
from backend.chatbot.chatbot import get_bot_response
from backend.chatbot.schema import chatbotRequest

#job and certs recommend
from backend.API.job_search import get_jobs_for_career
from backend.API.cert_recommend import get_certifications

#for visualization
from backend.visualize.trends import get_trends
from backend.visualize.skills import extract_skills_from_jobs, get_top_companies
from backend.visualize.visualization import plot_trend

app = FastAPI()

# 🔹 Endpoint 1: Form-based Career Prediction
@app.post("/predict-career/")
async def predict_career(data: StudentInput):
    input_dict = data.dict()

    # Default handling for missing optional fields
    input_dict.setdefault("degree", "Not Available")
    input_dict.setdefault("branch", "Not Available")
    input_dict.setdefault("cgpa", 0.0)
    input_dict.setdefault("skills", "Not Available")
    input_dict.setdefault("certifications", "Not Available")
    input_dict.setdefault("projects", "Not Available")

    # Predict careers
    df = pd.DataFrame([input_dict])
    top3 = predict_top_3_careers(df)
    input_dict["Predicted_Careers"] = [
        {"career": label, "confidence": round(score * 100, 2)} for label, score in top3
    ]

    # Save to MongoDB
    result = await students_collection.insert_one(input_dict)
    saved_doc = await students_collection.find_one({"_id": result.inserted_id})
    return {
        "Top_3_Career_Predictions": input_dict["Predicted_Careers"],
        "Saved_Data": serialize_mongo_document(saved_doc)
    }


# 🔹 Endpoint 2: Resume Upload → Parse → Predict
@app.post("/resume-career-predict/")
async def resume_predict(resume_file: UploadFile = File(...)):
    # Extract PDF text
    contents = await resume_file.read()
    pdf_text = ""
    try:
        with fitz.open(stream=contents, filetype="pdf") as doc:
            for page in doc:
                pdf_text += page.get_text()
    except Exception as e:
        return {"error": f"Failed to read PDF: {str(e)}"}

    # Parse resume with LLM
    parsed = parse_resume_text(pdf_text)

    # List of expected fields
    all_fields = [
        "Name", "Age", "Gender", "Email", "Degree", "Branch", "CGPA", "Personality_Type",
        "Preferred_Work_Style", "Skills", "Soft_Skills", "Interests", "Certifications",
        "Internship_Experience", "Career_Goal", "Favorite_Subjects", "Resume_Link"
    ]

    # Fill missing fields with defaults
    for field in all_fields:
        if field not in parsed or parsed[field] in [None, ""]:
            parsed[field] = "Not Available"

    try:
        parsed["CGPA"] = float(parsed["CGPA"]) if parsed["CGPA"] != "Not Available" else 0.0
        parsed["Age"] = int(parsed["Age"]) if parsed["Age"] != "Not Available" else 0
    except:
        parsed["CGPA"] = 0.0
        parsed["Age"] = 0

    # Model prediction input
    model_input = {
        "degree": parsed.get("Degree", "Not Available"),
        "branch": parsed.get("Branch", "Not Available"),
        "cgpa": parsed.get("CGPA", 0.0),
        "skills": parsed.get("Skills", "Not Available"),
        "certifications": parsed.get("Certifications", "Not Available"),
        "projects": parsed.get("Internship_Experience", "Not Available")
    }

    # Predict top 3 careers
    df = pd.DataFrame([model_input])
    top3 = predict_top_3_careers(df)
    parsed["Predicted_Careers"] = [
        {"career": label, "confidence": round(score * 100, 2)} for label, score in top3
    ]

    # Save to MongoDB
    result = await students_collection.insert_one(parsed)
    saved_doc = await students_collection.find_one({"_id": result.inserted_id})

    return {
        "Parsed_Profile": serialize_mongo_document(saved_doc),
        "Top_3_Career_Predictions": parsed["Predicted_Careers"]
    }


@app.post("/chatbot/")
async def chatbot_endpoint(request:chatbotRequest):
    user_message=request.query
    bot_reply=get_bot_response(user_message)
    return {"response ": bot_reply}


@app.get("/recommendations/{career}")
def get_recommendations(career: str,location: str = "India"):
    jobs = get_jobs_for_career(career,location)
    certs = get_certifications(career)
    
    return {
        "career": career,
        "jobs": jobs,
        "certifications": certs
    }




from fastapi.responses import JSONResponse

@app.get("/career-insights/{career}")
def career_insights(career: str):
    trends = get_trends(career)
    if "error" in trends:
        return JSONResponse(status_code=400, content=trends)

    skills = extract_skills_from_jobs(career)
    companies = get_top_companies(career)
    figs = plot_trend(trends["time"], trends["region"], skills, companies)

    return {
        "trends": {
            "time": trends['time'].to_dict(orient="records"),
            "region": trends['region'].to_dict(orient="records")
        },
        "skills": skills,
        "companies": companies,
        "charts": [fig.to_json() for fig in figs]
    }

