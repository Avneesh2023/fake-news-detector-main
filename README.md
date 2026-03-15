# Fake News Detector

An NLP-based fake news classifier achieving 99.6% accuracy.

## Tech Stack
- Python, scikit-learn, NLTK, spaCy
- TF-IDF Vectorization
- Ensemble Model (Logistic Regression + Naive Bayes + Passive-Aggressive)
- Flask REST API
- React Frontend

## How it works
1. Article text is preprocessed using NLTK and spaCy
2. Text is converted to numbers using TF-IDF
3. Three models vote on whether the article is FAKE or REAL
4. Result shown with confidence score and individual model votes

## Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python train_model.py
python app.py
```

## Results
- Accuracy: 99.6%
- F1 Score: 1.00
- Models: Logistic Regression, Naive Bayes, Passive-Aggressive
