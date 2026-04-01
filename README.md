📰 Fake News Detector (AI-Powered)

Python • Flask • React • NLP • Machine Learning • Hugging Face Deployment

An end-to-end AI-powered Fake News Detection system that analyzes news articles and classifies them as REAL or FAKE using an ensemble of machine learning models.
Deployed live using Hugging Face Spaces with a clean and responsive UI.

🚀 Live Demo

👉 Try it here:
🔗 https://aryan9170-fake-news-detector.hf.space/

✨ Key Features
🤖 Ensemble ML Model
Combines:
Logistic Regression
Naive Bayes
Passive-Aggressive Classifier
📊 Confidence Score
Displays prediction certainty (%)
🗳️ Model Voting System
Shows predictions from each individual model
⚡ Fast Inference
Results generated in under 2 seconds
📝 Live Text Analysis
Word count
Character count
🎨 Modern UI
Built with React for smooth user experience
🌐 Deployed on Hugging Face Spaces
No setup required — accessible anywhere
🛠️ Tech Stack
Layer	Technology
Language	Python 3
ML Models	scikit-learn
NLP	NLTK, spaCy
Vectorization	TF-IDF (5000 features, bigrams)
Backend	Flask (REST API)
Frontend	React.js
Deployment	Hugging Face Spaces
🧠 How It Works
Raw News Article
       │
       ▼
Text Preprocessing
 (spaCy + NLTK)
 • Lowercasing
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
Ensemble Model (Voting)
 ┌──────────────────────────┐
 │ Logistic Regression      │
 │ Naive Bayes              │
 │ Passive-Aggressive       │
 └──────────────────────────┘
       │
       ▼
Prediction:
REAL or FAKE + Confidence %
📊 Model Performance
Metric	Score
Accuracy	~96%
Precision	High
Recall	High
F1 Score	High

📌 Trained on 44,898 articles from the ISOT dataset:

21,417 real (Reuters)
23,481 fake news sources
⚙️ Run Locally
1️⃣ Clone Repository
git clone https://github.com/AryanStack91/fake-news-detector.git
cd fake-news-detector
2️⃣ Install Dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm
3️⃣ Add Dataset

Download dataset:
https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets

Place:

True.csv
Fake.csv
4️⃣ Train Model
python train_model.py
5️⃣ Run Backend
python app.py
6️⃣ Run Frontend
cd frontend
npm install
npm run build
cd ..
7️⃣ Open App
http://127.0.0.1:5000
🔌 API Reference
POST /predict
Request:
{
  "text": "Enter news article here..."
}
Response:
{
  "result": "FAKE",
  "confidence": 98.5,
  "votes": {
    "logistic_regression": "FAKE",
    "naive_bayes": "REAL",
    "passive_aggressive": "FAKE"
  }
}
📸 Screenshots
✅ Real News Detection
⚠️ Fake News Detection

(Add screenshots here for better GitHub appeal)

🗂️ Dataset
📦 ISOT Fake News Dataset
44,898 total articles
Sources:
Reuters (Real)
PolitiFact & others (Fake)
🔮 Future Improvements
🔗 Integration with live news APIs
🤖 Advanced AI recommendations
🌍 Multilingual support
📱 Mobile optimization
🧠 Deep Learning models (LSTM / BERT)
👨‍💻 Author

Aryan Prajapati
🔗 GitHub: https://github.com/AryanStack91

📄 License

MIT License — free to use for learning and projects.
