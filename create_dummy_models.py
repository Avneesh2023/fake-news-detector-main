import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, PassiveAggressiveClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import MaxAbsScaler

def train_dummy():
    # Load dummy data
    try:
        df = pd.read_csv('train.csv').fillna('')
    except FileNotFoundError:
        print("Please run create_mock_data.py first to generate train.csv.")
        return
        
    df['content'] = df['title'] + ' ' + df['text']
    
    # We will bypass complex preprocessing to keep it simple and avoid spacy
    X = df['content'].str.lower()
    y = df['label']
    
    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_tfidf = vectorizer.fit_transform(X)
    
    # Scaler
    scaler = MaxAbsScaler()
    X_scaled = scaler.fit_transform(X_tfidf)
    
    # Models
    lr = LogisticRegression(max_iter=1000, C=1.0)
    nb = MultinomialNB(alpha=0.1)
    pac = PassiveAggressiveClassifier(max_iter=50)
    
    lr.fit(X_scaled, y)
    nb.fit(X_scaled, y)
    pac.fit(X_scaled, y)
    
    ensemble = VotingClassifier(
        estimators=[('lr', lr), ('nb', nb), ('pac', pac)],
        voting='hard'
    )
    ensemble.fit(X_scaled, y)
    
    # Save dummy models
    joblib.dump(ensemble, 'fake_news_model.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("Dummy models created successfully: fake_news_model.pkl, tfidf_vectorizer.pkl, scaler.pkl")

if __name__ == '__main__':
    train_dummy()
