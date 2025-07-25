# import streamlit as st
# from components.career_predict import show_career_form
# from components.resume_predict import show_resume_upload
# from components.job_cert_recommend import show_job_cert
# from components.trends_visualizer import show_trends
# from utils.session_state import get_session

# st.set_page_config(page_title="Smart Career Guidance", layout="wide")
# session = get_session()

# st.title("🚀 Smart Career Guidance System")

# menu = ["Career Form", "Resume Upload", "Job & Cert Recommendations", "Career Trends"]
# choice = st.sidebar.selectbox("📂 Navigate", menu)

# st.sidebar.markdown("---")
# st.sidebar.write("👤 Welcome!")
# # Optional Login-Sim
# # st.sidebar.text_input("Username")
# # st.sidebar.text_input("Password", type="password")

# if choice == "Career Form":
#     show_career_form()

# elif choice == "Resume Upload":
#     show_resume_upload()

# elif choice == "Job & Cert Recommendations":
#     show_job_cert()

# elif choice == "Career Trends":
#     show_trends()

# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px
# from streamlit_lottie import st_lottie

# # -------------------- LOTTIE ANIMATION LOADER --------------------
# def load_lottie_url(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # -------------------- CUSTOM CSS --------------------
# def inject_custom_css():
#     st.markdown("""
#         <style>
#         .reportview-container {
#             animation: fadein 1s;
#         }
#         @keyframes fadein {
#             from { opacity: 0; }
#             to   { opacity: 1; }
#         }
#         h1, h2, h3 {
#             color: #5e17eb !important;
#         }
#         .stButton>button {
#             background-color: #5e17eb;
#             color: white;
#             border-radius: 8px;
#         }
#         </style>
#     """, unsafe_allow_html=True)

# inject_custom_css()

# # -------------------- PAGE CONFIG --------------------
# st.set_page_config(page_title="Smart Career Guidance", layout="wide")

# # -------------------- SIDEBAR --------------------
# st.sidebar.title("🧠 Career Navigator")
# page = st.sidebar.radio("Navigate", ["Career Predictor", "Upload Resume", "Career Trends"])
# mode = st.sidebar.selectbox("🌗 Theme", ["Light", "Dark"])
# if mode == "Dark":
#     st.markdown("""<style>body { background-color: #0e1117; color: white; }</style>""", unsafe_allow_html=True)

# st.sidebar.markdown("---")
# st.sidebar.info("Built with ❤️ using FastAPI + Streamlit")

# # -------------------- MAIN PAGE --------------------
# st.title("🎓 Smart Career Guidance System")

# if page == "Career Predictor":
#     st.subheader("🔮 Predict Your Top 3 Career Options")
#     degree = st.text_input("Degree")
#     branch = st.text_input("Branch")
#     cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
#     skills = st.text_area("Skills")
#     certifications = st.text_area("Certifications")
#     projects = st.text_area("Project Experience")

#     if st.button("🎯 Predict Careers"):
#         data = {
#             "degree": degree,
#             "branch": branch,
#             "cgpa": cgpa,
#             "skills": skills,
#             "certifications": certifications,
#             "projects": projects
#         }
#         res = requests.post("http://localhost:8000/predict-career/", json=data)
#         if res.status_code == 200:
#             response = res.json()
#             st.success("Top 3 Recommended Careers:")
#             for item in response["Top_3_Career_Predictions"]:
#                 st.write(f"✅ {item['career']} ({item['confidence']}%)")
#             with st.expander("🔍 Saved Data"):
#                 st.json(response["Saved_Data"])
#         else:
#             st.error("Prediction failed. Check FastAPI server.")

# elif page == "Upload Resume":
#     st.subheader("📄 Upload Your Resume")
#     resume = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

#     if resume and st.button("🔍 Analyze Resume"):
#         files = {"resume_file": resume}
#         res = requests.post("http://localhost:8000/resume-career-predict/", files=files)
#         if res.status_code == 200:
#             parsed = res.json()
#             st.success("Top 3 Recommended Careers:")
#             for item in parsed["Top_3_Career_Predictions"]:
#                 st.write(f"✅ {item['career']} ({item['confidence']}%)")
#             with st.expander("🔍 Parsed Resume Data"):
#                 st.json(parsed["Parsed_Profile"])
#         else:
#             st.error("Resume parsing failed.")

# elif page == "Career Trends":
#     st.subheader("📈 Career Trend Insights")
#     career = st.text_input("Enter Career Name", "Data Science")
#     if st.button("📊 Show Trends"):
#         res = requests.get(f"http://localhost:8000/career-insights/{career}")
#         if res.status_code == 200:
#             data = res.json()

#             tab1, tab2, tab3, tab4 = st.tabs(["📌 Skills", "🏢 Companies", "📈 Over Time", "🌍 By Region"])

#             with tab1:
#                 skills_data = data["skills"]
#                 if skills_data:
#                     skills, counts = zip(*skills_data)
#                     fig = px.bar(x=skills, y=counts, title="Top Skills")
#                     st.plotly_chart(fig)
#                 else:
#                     st.warning("No skill data available for this career.")
                                

#             with tab2:
#                 comps, comp_counts = zip(*data['companies'])
#                 st.plotly_chart(px.bar(x=comps, y=comp_counts, title="Top Hiring Companies"))

#             with tab3:
#                 time_df = pd.DataFrame(data["trends"]["time"])
#                 st.plotly_chart(px.line(time_df, x='date', y=time_df.columns[1], title="Interest Over Time"))

#             with tab4:
#                 region_df = pd.DataFrame(data["trends"]["region"])
#                 st.plotly_chart(px.bar(region_df, x='geoName', y=region_df.columns[1], title="Regional Interest"))
#         else:
#             st.error("Trend data fetch failed")



# # Optional Lottie Animation
# with st.container():
#     st_lottie(load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_pprxh53t.json"), height=200, key="ai")


import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie

# -------------------- LOTTIE ANIMATION LOADER --------------------
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -------------------- CUSTOM CSS --------------------
def inject_custom_css():
    st.markdown("""
        <style>
        .reportview-container {
            animation: fadein 1s;
        }
        @keyframes fadein {
            from { opacity: 0; }
            to   { opacity: 1; }
        }
        h1, h2, h3 {
            color: #5e17eb !important;
        }
        .stButton>button {
            background-color: #5e17eb;
            color: white;
            border-radius: 8px;
        }
        .chatbot-container {
            position: fixed;
            top: 10px;
            right: 20px;
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.15);
            z-index: 999;
            width: 300px;
        }
        </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Smart Career Guidance", layout="wide")

# -------------------- SIDEBAR --------------------
st.sidebar.title("🧠 Career Navigator")
page = st.sidebar.radio("Navigate", [
    "Career Predictor", 
    "Upload Resume", 
    "Career Trends", 
    "Job & Cert Recommendations"
])
mode = st.sidebar.selectbox("🌗 Theme", ["Light", "Dark"])
if mode == "Dark":
    st.markdown("""<style>body { background-color: #0e1117; color: white; }</style>""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("Built with ❤️ using FastAPI + Streamlit")

# -------------------- MAIN PAGE --------------------
st.title("🎓 Smart Career Guidance System")

if page == "Career Predictor":
    st.subheader("🔮 Predict Your Top 3 Career Options")
    degree = st.text_input("Degree")
    branch = st.text_input("Branch")
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
    skills = st.text_area("Skills")
    certifications = st.text_area("Certifications")
    projects = st.text_area("Project Experience")

    if st.button("🎯 Predict Careers"):
        data = {
            "degree": degree,
            "branch": branch,
            "cgpa": cgpa,
            "skills": skills,
            "certifications": certifications,
            "projects": projects
        }
        res = requests.post("http://localhost:8000/predict-career/", json=data)
        if res.status_code == 200:
            response = res.json()
            st.success("Top 3 Recommended Careers:")
            for item in response["Top_3_Career_Predictions"]:
                st.write(f"✅ {item['career']} ({item['confidence']}%)")
            with st.expander("🔍 Saved Data"):
                st.json(response["Saved_Data"])
        else:
            st.error("Prediction failed. Check FastAPI server.")

elif page == "Upload Resume":
    st.subheader("📄 Upload Your Resume")
    resume = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

    if resume and st.button("🔍 Analyze Resume"):
        files = {"resume_file": resume}
        res = requests.post("http://localhost:8000/resume-career-predict/", files=files)
        if res.status_code == 200:
            parsed = res.json()
            st.success("Top 3 Recommended Careers:")
            for item in parsed["Top_3_Career_Predictions"]:
                st.write(f"✅ {item['career']} ({item['confidence']}%)")
            with st.expander("🔍 Parsed Resume Data"):
                st.json(parsed["Parsed_Profile"])
        else:
            st.error("Resume parsing failed.")

elif page == "Career Trends":
    st.subheader("📈 Career Trend Insights")
    career = st.text_input("Enter Career Name", "Data Science")
    if st.button("📊 Show Trends"):
        res = requests.get(f"http://localhost:8000/career-insights/{career}")
        if res.status_code == 200:
            data = res.json()

            tab1, tab2, tab3, tab4 = st.tabs(["📌 Skills", "🏢 Companies", "📈 Over Time", "🌍 By Region"])

            with tab1:
                skills_data = data["skills"]
                if skills_data:
                    skills, counts = zip(*skills_data)
                    fig = px.bar(x=skills, y=counts, title="Top Skills")
                    st.plotly_chart(fig)
                else:
                    st.warning("No skill data available for this career.")
                             
            with tab2:
                comps, comp_counts = zip(*data['companies'])
                st.plotly_chart(px.bar(x=comps, y=comp_counts, title="Top Hiring Companies"))

            with tab3:
                time_df = pd.DataFrame(data["trends"]["time"])
                st.plotly_chart(px.line(time_df, x='date', y=time_df.columns[1], title="Interest Over Time"))

            with tab4:
                region_df = pd.DataFrame(data["trends"]["region"])
                st.plotly_chart(px.bar(region_df, x='geoName', y=region_df.columns[1], title="Regional Interest"))
        else:
            st.error("Trend data fetch failed")

elif page == "Job & Cert Recommendations":
    st.subheader("💼 Job & 📚 Certification Recommendations")
    career = st.text_input("🔍 Enter Career (e.g., Data Scientist)", "Data Scientist")

    if st.button("Get Recommendations"):
        try:
            res = requests.get(f"http://localhost:8000/recommendations/{career}")
            if res.status_code == 200:
                data = res.json()

                st.markdown("### 💼 Job Listings")
                for job in data.get("jobs", []):
                    title = job.get("title", "No Title")
                    company = job.get("company", "")
                    location = job.get("location", "")
                    link = job.get("link", "")

                    if link and link != "#":
                        st.markdown(f"- **{title}** at *{company}* ({location}) — [Apply Here]({link})")
                    else:
                        st.markdown(f"- **{title}** at *{company}* ({location})")

                st.markdown("### 📘 Best Online Certifications")
                for cert in data.get("certifications", []):
                    cert_name = cert.get("name", "Certification")
                    cert_link = cert.get("link", "#")
                    st.markdown(f"- [{cert_name}]({cert_link})")
            else:
                st.error("❌ Failed to fetch recommendations.")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

# -------------------- CONSISTENT CHATBOT --------------------
with st.container():
    st.markdown("""
        <div class="chatbot-container">
            <h4>💬 Chatbot Assistant</h4>
        </div>
    """, unsafe_allow_html=True)
    user_message = st.text_input("Ask your assistant:", key="chat_input")
    if st.button("Send", key="chat_send"):
        try:
            res = requests.post("http://localhost:8000/chatbot/", json={"query": user_message})
            if res.status_code == 200:
                st.write("Bot:", res.json().get("response ", "No response"))
            else:
                st.error("Bot failed to respond.")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

# -------------------- LOTTIE ANIMATION --------------------
with st.container():
    st_lottie(load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_pprxh53t.json"), height=200, key="ai")
