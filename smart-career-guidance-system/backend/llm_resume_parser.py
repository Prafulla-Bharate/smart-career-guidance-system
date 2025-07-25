import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest", temperature=0)
prompt = PromptTemplate.from_template("""
Extract the following fields from the resume text:
Name, Age, Gender, Email, Degree, Branch, CGPA, Personality_Type, Preferred_Work_Style, Skills,
Soft_Skills, Interests, Certifications, Internship_Experience, Career_Goal, Favorite_Subjects, Resume_Link

If any field is missing, return "Not Available".

Text: {resume_text}
""")

chain = prompt | llm

def parse_resume_text(resume_text: str) -> dict:
    parsed = chain.invoke({"resume_text": resume_text})
    response = parsed.content

    output = {}
    for line in response.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            output[key.strip()] = val.strip()
    return output
