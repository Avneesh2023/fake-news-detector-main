📰 Fake News Detector
Python Flask React Accuracy GitHub

An end-to-end NLP-powered fake news detection system with a React frontend and Flask REST API backend. Built using an ensemble of three machine learning models achieving 96% accuracy on 44,000+ news articles.

🚀 Live Demo
👉 https://aryan9170-fake-news-detector.hf.space/

🚀 Live Demo
⚡ Run locally using the setup instructions below, then expose publicly using ngrok.

Start Flask

python app.py

Expose publicly

.\ngrok.exe http 5000

✨ Features
🤖 Ensemble Model — Logistic Regression + Naive Bayes + Passive-Aggressive voting classifier
📊 Confidence Score — Shows how confident the model is in its prediction
🗳️ Individual Model Votes — See what each model thinks independently
📝 Word & Character Counter — Real-time article length tracking
⚡ Fast Predictions — Results in under 2 seconds
🎨 Clean React UI — Modern responsive frontend

🛠️ Tech Stack
Layer Technology
Language Python 3.10
ML Models scikit-learn
NLP NLTK, spaCy
Vectorization TF-IDF (5000 features, bigrams)
Backend Flask REST API
Frontend React.js
Tunneling ngrok

📁 Project Structure
fake-news-detector/
├── app.py ← Flask REST API
├── train_model.py ← Model training script
├── requirements.txt ← Python dependencies
├── build.sh ← Render build script
├── render.yaml ← Render deployment config
└── frontend/
├── src/
│ └── App.js ← React frontend
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
│ Logistic Regression │
│ Naive Bayes │
│ Passive-Aggressive │
└─────────────────────────────┘
│
▼
REAL or FAKE + Confidence %

📊 Model Performance
Metric Before spaCy After spaCy
F1 Score 0.99 1.00
Accuracy 99.2% 99.6%
Precision 0.99 1.00
Recall 0.99 1.00

Trained on 44,898 articles from the ISOT Fake News Dataset (21,417 real articles from Reuters + 23,481 fake articles)

⚙️ Setup & Installation

Clone the repository
git clone https://github.com/AryanStack91/fake-news-detector.git

cd fake-news-detector
Install Python dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm
Download the dataset
Download the ISOT Fake News Dataset and place True.csv and Fake.csv in the project folder.

Dataset: https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets

Train the model
python train_model.py

This will create:
fake_news_model.pkl
tfidf_vectorizer.pkl
scaler.pkl

Build React frontend
cd frontend
npm install
npm run build
cd ..
Run the app
python app.py

Open http://127.0.0.1:5000
 in your browser.

Expose publicly with ngrok (optional)
.\ngrok.exe http 5000

Share the generated URL with anyone!

🔌 API Reference

POST /predict
Analyse a news article and return prediction.

Request:

{
"text": "Your news article text here..."
}

Response:

{
"result": "FAKE",
"confidence": 100,
"votes": {
"logistic_regression": "FAKE",
"naive_bayes": "FAKE",
"passive_aggressive": "FAKE"
}
}

📸 Screenshots
✅ Real news detection
Real News

⚠️ Fake news detection
Fake News

🗂️ Dataset
ISOT Fake News Dataset

44,898 total articles
Real news sourced from Reuters.com
Fake news sourced from PolitiFact & other fact-checking sites
Topics: politics, world news, US news

👨‍💻 Author
Aryan Prajapati — GitHub

📄 License
MIT License — feel free to use this project for learning!
