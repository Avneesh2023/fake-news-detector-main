# 📰 Fake News Detector

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-REST%20API-lightgrey)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Accuracy](https://img.shields.io/badge/Accuracy-96%25-brightgreen)
![GitHub](https://img.shields.io/badge/GitHub-AryanStack91-black)

An end-to-end NLP-powered fake news detection system with a React frontend
and Flask REST API backend. Built using an ensemble of three machine learning
models achieving 96% accuracy on 44,000+ news articles.

---

## 🚀 Live Demo

> ⚡ Run locally using the setup instructions below, then expose publicly using ngrok.
```bash
# Start Flask
python app.py

# Expose publicly
.\ngrok.exe http 5000
```

---

## ✨ Features

- 🤖 **Ensemble Model** — Logistic Regression + Naive Bayes + Passive-Aggressive voting classifier
- 📊 **Confidence Score** — Shows how confident the model is in its prediction
- 🗳️ **Individual Model Votes** — See what each model thinks independently
- 📝 **Word & Character Counter** — Real-time article length tracking
- ⚡ **Fast Predictions** — Results in under 2 seconds
- 🎨 **Clean React UI** — Modern responsive frontend

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10 |
| ML Models | scikit-learn |
| NLP | NLTK, spaCy |
| Vectorization | TF-IDF (5000 features, bigrams) |
| Backend | Flask REST API |
| Frontend | React.js |
| Tunneling | ngrok |

---

## 📁 Project Structure
```
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
```

---

## 🧠 How It Works
```
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
```

---

## 📊 Model Performance

| Metric | Before spaCy | After spaCy |
|--------|-------------|-------------|
| F1 Score | 0.99 | 1.00 |
| Accuracy | 99.2% | 99.6% |
| Precision | 0.99 | 1.00 |
| Recall | 0.99 | 1.00 |

Trained on **44,898 articles** from the ISOT Fake News Dataset
(21,417 real articles from Reuters + 23,481 fake articles)

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/AryanStack91/fake-news-detector.git
cd fake-news-detector
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Download the dataset
Download the ISOT Fake News Dataset and place `True.csv`
and `Fake.csv` in the project folder.

Dataset: https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets

### 4. Train the model
```bash
python train_model.py
```

This will create:
- `fake_news_model.pkl`
- `tfidf_vectorizer.pkl`
- `scaler.pkl`

### 5. Build React frontend
```bash
cd frontend
npm install
npm run build
cd ..
```

### 6. Run the app
```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

### 7. Expose publicly with ngrok (optional)
```bash
.\ngrok.exe http 5000
```

Share the generated URL with anyone!

---

## 🔌 API Reference

### POST /predict

Analyse a news article and return prediction.

**Request:**
```json
{
  "text": "Your news article text here..."
}
```

**Response:**
```json
{
  "result": "FAKE",
  "confidence": 100,
  "votes": {
    "logistic_regression": "FAKE",
    "naive_bayes": "FAKE",
    "passive_aggressive": "FAKE"
  }
}
```

---

## 📸 Screenshots

### ✅ Real news detection
![Real News](https://i.imgur.com/placeholder1.png)

### ⚠️ Fake news detection
![Fake News](https://i.imgur.com/placeholder2.png)

---

## 🗂️ Dataset

**ISOT Fake News Dataset**
- 44,898 total articles
- Real news sourced from Reuters.com
- Fake news sourced from PolitiFact & other fact-checking sites
- Topics: politics, world news, US news

---

## 👨‍💻 Author

**Aryan Prajapati** — [GitHub](https://github.com/AryanStack91)

---

## 📄 License

MIT License — feel free to use this project for learning!
