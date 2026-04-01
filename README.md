📰 Fake News Detector
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask"> <img src="https://img.shields.io/badge/React-Frontend-blue?style=for-the-badge&logo=react"> <img src="https://img.shields.io/badge/Accuracy-96%25-brightgreen?style=for-the-badge"> </p>

An end-to-end NLP-powered Fake News Detection system with a React frontend and Flask REST API backend.
Built using an ensemble of three machine learning models achieving ~96% accuracy on 44,000+ news articles.

🚀 Live Demo

👉 Try it here:
🔗 https://aryan9170-fake-news-detector.hf.space/

⚡ No setup required — fully deployed on Hugging Face Spaces.

✨ Features
🤖 Ensemble Model — Logistic Regression + Naive Bayes + Passive-Aggressive voting classifier
📊 Confidence Score — Shows how confident the model is in its prediction
🗳️ Individual Model Votes — See what each model predicts independently
📝 Word & Character Counter — Real-time article length tracking
⚡ Fast Predictions — Results in under 2 seconds
🎨 Clean React UI — Modern responsive frontend
🛠️ Tech Stack
Layer	Technology
Language	Python 3.10
ML Models	scikit-learn
NLP	NLTK, spaCy
Vectorization	TF-IDF (5000 features, bigrams)
Backend	Flask REST API
Frontend	React.js
Deployment	Hugging Face Spaces
(Optional) Tunneling	ngrok
📁 Project Structure
fake-news-detector/
├── app.py                  ← Flask REST API
├── train_model.py          ← Model training script
├── requirements.txt        ← Python dependencies
├── build.sh                ← Render build script
├── render.yaml             ← Render deployment config
└── frontend/
    ├── src/
    │   └── App.js          ← React frontend
    └── public/
        └── index.html
🧠 How It Works
Raw Article Text
      │
      ▼
Text Preprocessing (spaCy + NLTK)
  • Lowercase
  • Remove URLs & punctuation
  • Lemmatization
  • Stopword removal
      │
      ▼
TF-IDF Vectorization
  • 5000 features
  • Unigrams + Bigrams
      │
      ▼
Ensemble Model (Majority Voting)
  ┌─────────────────────────────┐
  │ Logistic Regression         │
  │ Naive Bayes                 │
  │ Passive-Aggressive          │
  └─────────────────────────────┘
      │
      ▼
  REAL or FAKE + Confidence %
📊 Model Performance
Metric	Score
Accuracy	~96%
Precision	High
Recall	High
F1 Score	High

📌 Trained on 44,898 articles from the ISOT Fake News Dataset:

21,417 real articles (Reuters)
23,481 fake articles
⚙️ Setup & Installation
1. Clone the repository
git clone https://github.com/AryanStack91/fake-news-detector.git
cd fake-news-detector
2. Install Python dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm
3. Download the dataset

Download the ISOT dataset and place True.csv and Fake.csv in the project folder

🔗 https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets

4. Train the model
python train_model.py

This will create:

fake_news_model.pkl
tfidf_vectorizer.pkl
scaler.pkl
5. Build React frontend
cd frontend
npm install
npm run build
cd ..
6. Run the app
python app.py

Open 👉 http://127.0.0.1:5000

7. Expose publicly with ngrok (optional)
.\ngrok.exe http 5000
🔌 API Reference
POST /predict

Analyse a news article and return prediction

Request:
{
  "text": "Your news article text here..."
}
Response:
{
  "result": "FAKE",
  "confidence": 98.5,
  "votes": {
    "logistic_regression": "FAKE",
    "naive_bayes": "FAKE",
    "passive_aggressive": "FAKE"
  }
}
📸 Screenshots

✅ Real news detection
(Add screenshot here)

⚠️ Fake news detection
(Add screenshot here)

🗂️ Dataset

ISOT Fake News Dataset

44,898 total articles
Real news: Reuters
Fake news: PolitiFact & other sources
Topics: politics, world news, US news
👨‍💻 Author

Aryan Prajapati
🔗 https://github.com/AryanStack91

📄 License

MIT License — feel free to use this project for learning!

⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub!
