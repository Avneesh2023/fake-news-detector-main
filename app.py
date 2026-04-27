from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import re
import os
from nltk.corpus import stopwords

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

model      = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
scaler     = joblib.load('scaler.pkl')
stops      = set(stopwords.words('english'))

def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = [word for word in text.split() if word not in stops]
    return ' '.join(tokens)

@app.route('/predict', methods=['POST'])
def predict():
    data    = request.get_json()
    article = data.get('text', '')

    if not article.strip():
        return jsonify({'error': 'No text provided'}), 400

    cleaned    = preprocess(article)
    vectorized = vectorizer.transform([cleaned])
    scaled     = scaler.transform(vectorized)
    prediction = model.predict(scaled)[0]

    votes = [
        model.estimators_[0].predict(scaled)[0],
        model.estimators_[1].predict(scaled)[0],
        model.estimators_[2].predict(scaled)[0],
    ]
    confidence = round((votes.count(prediction) / 3) * 100)
    result     = 'FAKE' if prediction == 1 else 'REAL'

    return jsonify({
        'result':     result,
        'confidence': confidence,
        'votes': {
            'logistic_regression': 'FAKE' if votes[0] == 1 else 'REAL',
            'naive_bayes':         'FAKE' if votes[1] == 1 else 'REAL',
            'passive_aggressive':  'FAKE' if votes[2] == 1 else 'REAL',
        }
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
