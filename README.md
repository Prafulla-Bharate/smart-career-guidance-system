# 🎓 Smart Career Guidance System

A full-fledged AI-powered career recommendation platform built using **FastAPI + Streamlit**. It predicts top careers from user profile or resume, recommends trending jobs and certifications, visualizes Google trends, and offers an AI chatbot assistant.

---


---

## 📷 Screenshots

### 🔮 Career Predictor
![Career Predictor](../img/career-trends.png)(../img/front.png)

Predict top 3 careers from your academic and skill profile.

### 📄 Resume Analysis
![Resume Upload](../img/resume.png)
Parse PDF resumes and get top career predictions.

### 📈 Career Trend Insights
![Career Trends](../img/career-trends2.png)
![](../img/career-trends2.png)
![](../img/career-trends3.png)
Google Trends, Skills, Hiring Companies for any career.

### 💼 Jobs & 📚 Certification Recommendations
![Jobs & Certs](../img/job-cert-recommend.png)
Get real-time job listings and online course suggestions.

### 🤖 Chatbot Assistant
![Chatbot](../img/chatbot.png)
Talk with the built-in AI chatbot to ask career questions.

---

## 🧠 Features

- 🎓 Predict top 3 careers using AI
- 📄 Upload and analyze resumes (PDF)
- 📈 Google Trends + Skills + Companies
- 💼 Realtime Job listings (via API scraping)
- 📚 Certification suggestions
- 🤖 Built-in Chatbot Assistant
- 🌗 Dark/Light themes
- 🎨 Modern UI with animations (Lottie)

---

## 🛠️ Technologies Used

| Frontend     | Backend    | AI/ML       | Tools & APIs         |
|--------------|------------|-------------|----------------------|
| Streamlit    | FastAPI    | XGBoost     | Google Trends API    |
| Lottie       | Uvicorn    | SentenceTransformer | Job Scraping     |
| Plotly       |            | Pickle Models | OpenAI/Gemini Chat  |

---

## 📁 Folder Structure

```bash
smart-career-guidance-system/
├── backend/
│   ├── main.py                  # FastAPI backend
│   ├── recommendation.py        # Jobs/Cert API
│   ├── trends.py, skills.py     # Google Trends/skills
│   └── chatbot.py               # Chat endpoint
├── frontend/
│   └── app.py                   # Streamlit app
├── model/
│   ├── model.pkl, scaler.pkl, encoder.pkl
│   └── clean_balanced_student.csv


---

## ▶️ How To Run

### 🔧 1. Clone the Project
```bash
git clone https://github.com/yourusername/smart-career-guidance-system
cd smart-career-guidance-system
```

### ⚙️ 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 🧠 3. Start Backend (FastAPI)
```bash
uvicorn backend.main:app --reload
```

### 🖥️ 4. Start Frontend (Streamlit)
```bash
cd frontend
streamlit run app.py
```


---


---

## 🌐 API Endpoints

| Endpoint                        | Description                         |
|-------------------------------|-------------------------------------|
| `/predict-career/`           | Predicts top 3 careers              |
| `/resume-career-predict/`    | Parses PDF & predicts               |
| `/recommendations/{career}`  | Returns jobs & certifications       |
| `/career-insights/{career}`  | Google trends, skills, companies    |
| `/chatbot/`                  | Responds to user chat queries       |

---

## 📌 Sample Usage (Chatbot)
```json
POST /chatbot/
{
  "query": "What are the best careers for someone with Python and ML skills?"
}
```

---

## 🧑‍💻 Contributors

- [Prafulla Bharate](https://github.com/Prafulla-Bharate)

---

## 📜 License
MIT License

---


