💡 Smart Career Guidance System
A machine learning-based web application built with Streamlit that recommends the most suitable career paths based on a student's academic stream, skills, interests, certifications, and CGPA. This system leverages multi-label encoding, a trained classification model, and real-time job trend data to deliver personalized, data-driven career guidance.

🚀 Features
🔮 Career Prediction: Based on academic and personal input or uploaded resume

🧠 Machine Learning Model: Trained classification model using scikit-learn

📑 Resume Parsing: Extracts relevant keywords (skills, interests, certs) from .txt or .pdf files

🌐 Job Trend Fetching: Live job trend data from RapidAPI JSearch

📊 Confidence Score Visualization: Displays top 3 predictions with confidence bar chart

🎓 Course Suggestions: Auto-recommended Coursera and Udemy links for skill development

🛠️ Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python, scikit-learn, NLTK
Visualization	Matplotlib, Seaborn
NLP	NLTK (tokenizer, word cleaner)
APIs	RapidAPI (JSearch for job data)
Model Persistence	Joblib

📷 Screenshots
Manual Input Form	Resume Upload Parsing

🧑‍💻 How to Run Locally
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/yourusername/smart-career-guidance.git
cd smart-career-guidance

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app1.py
⚠️ Note: Ensure career_model.pkl and encoder .pkl files are in the same directory.

📁 Dataset and Model
Trained on a synthetic/collected dataset of student profiles

Multi-class classification model (e.g., Random Forest or Logistic Regression)

Label encoders used for categorical and multi-label fields

✅ Future Enhancements
🔐 User login system for personalized history

☁️ Hosting on Streamlit Cloud or Render

🧾 Integration with LinkedIn Resume parser API

🧠 Upgrade to Deep Learning with TensorFlow or PyTorch

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙋‍♂️ Author
Prafulla Bharate
Data Science | Machine Learning | Web Apps
LinkedIn • GitHub
