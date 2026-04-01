📰 Fake News Detector 🚀
<p align="center"> <b>AI-Powered Fake News Detection System</b><br> <i>Flask • React • NLP • Machine Learning • Hugging Face</i> </p> <p align="center"> <a href="https://aryan9170-fake-news-detector.hf.space/"> <img src="https://img.shields.io/badge/Live%20Demo-Click%20Here-blue?style=for-the-badge&logo=vercel"> </a> <a href="https://github.com/AryanStack91/fake-news-detector"> <img src="https://img.shields.io/github/stars/AryanStack91/fake-news-detector?style=for-the-badge"> </a> <img src="https://img.shields.io/badge/Accuracy-96%25-brightgreen?style=for-the-badge"> <img src="https://img.shields.io/badge/Made%20With-Python%20%7C%20React-orange?style=for-the-badge"> </p>
🚀 Live Demo
<p align="center"> <a href="https://aryan9170-fake-news-detector.hf.space/"> <img src="https://img.shields.io/badge/Try%20Now-Hugging%20Face-yellow?style=for-the-badge&logo=huggingface"> </a> </p>
🎯 Project Overview

An end-to-end NLP-based Fake News Detection system that classifies news articles as REAL or FAKE using an ensemble of machine learning models.

✨ Designed with:

⚡ Fast predictions
🎨 Clean UI
🤖 Explainable AI (model votes + confidence)
🎥 Demo Preview (Add your GIF here)
<p align="center"> <img src="https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif" width="700"/> </p>

👉 Replace this GIF with your actual project demo (I can help you create one)

✨ Features
🤖 Ensemble Learning
Logistic Regression
Naive Bayes
Passive-Aggressive
📊 Confidence Score (%)
🗳️ Model Voting Visualization
⚡ < 2s Prediction Speed
📝 Live Text Stats
Word count
Character count
🎨 Responsive React UI
🌐 Deployed on Hugging Face Spaces
🧠 System Architecture
User Input (News Article)
        │
        ▼
Text Preprocessing (spaCy + NLTK)
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Ensemble Model (Voting)
        │
        ▼
REAL / FAKE + Confidence Score
🛠️ Tech Stack
<p align="center"> <img src="https://skillicons.dev/icons?i=python,flask,react,sklearn,git" /> </p>
Layer	Technology
Language	Python
Backend	Flask
Frontend	React.js
ML Models	scikit-learn
NLP	spaCy, NLTK
Deployment	Hugging Face
📊 Model Performance
<p align="center"> <img src="https://img.shields.io/badge/Accuracy-96%25-brightgreen?style=for-the-badge"> <img src="https://img.shields.io/badge/Dataset-44K%2B%20Articles-blue?style=for-the-badge"> </p>
📦 Dataset: ISOT Fake News Dataset
📰 44,898 articles
🧠 Balanced classification performance
⚙️ Local Setup
# Clone repo
git clone https://github.com/AryanStack91/fake-news-detector.git
cd fake-news-detector

# Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Train model
python train_model.py

# Run backend
python app.py

Frontend:

cd frontend
npm install
npm run build
🔌 API Usage
POST /predict
{
  "text": "News article here..."
}
Response:
{
  "result": "REAL",
  "confidence": 97.3,
  "votes": {
    "logistic_regression": "REAL",
    "naive_bayes": "REAL",
    "passive_aggressive": "FAKE"
  }
}
🔮 Future Enhancements
🌍 Multilingual Fake News Detection
🔗 Live News API Integration
🤖 Deep Learning (BERT / LSTM)
📱 Mobile App Version
📊 Analytics Dashboard
👨‍💻 Author

Aryan Prajapati

<p align="center"> <a href="https://github.com/AryanStack91"> <img src="https://img.shields.io/badge/GitHub-AryanStack91-black?style=for-the-badge&logo=github"> </a> </p>
⭐ Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Share it with others
👉 Add it to your portfolio

📄 License

MIT License
