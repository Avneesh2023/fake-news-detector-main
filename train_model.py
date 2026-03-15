# # import pandas as pd

# # # Load both files
# # true_df = pd.read_csv('True.csv')
# # fake_df = pd.read_csv('Fake.csv')

# # # Check what columns exist
# # print("True columns:", true_df.columns.tolist())
# # print("Fake columns:", fake_df.columns.tolist())
# # print("True shape:", true_df.shape)
# # print("Fake shape:", fake_df.shape)

# # # Add label: 0 = real, 1 = fake
# # true_df['label'] = 0
# # fake_df['label'] = 1

# # # Combine into one dataframe
# # df = pd.concat([true_df, fake_df], ignore_index=True)

# # print("Total articles:", len(df))
# # print(df['label'].value_counts())
# # # 0 (real) → ~21417
# # # 1 (fake) → ~23481


# # # Shuffle so real and fake are mixed (important!)
# # df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# # # Fill any missing values
# # df = df.fillna('')

# # # Combine title + text
# # df['content'] = df['title'] + ' ' + df['text']

# # print("Dataset ready:", df.shape)
# # print(df[['title', 'label']].head(5))

# # # Save combined dataset
# # df.to_csv('train.csv', index=False)
# # print("Saved as train.csv!")

# # train_model.py
# import pandas as pd
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer

# # Download required NLTK data (only needed once)
# nltk.download('stopwords')

# # Load your combined dataset
# df = pd.read_csv('train.csv')
# df = df.fillna('')
# df['content'] = df['title'] + ' ' + df['text']

# print("Loaded:", len(df), "articles")

# # Setup
# stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()

# def preprocess(text):
#     text = str(text).lower()                        # lowercase
#     text = re.sub(r'http\S+|www\S+', '', text)      # remove URLs
#     text = re.sub(r'[^a-z\s]', '', text)            # remove punctuation/numbers
#     tokens = text.split()
#     tokens = [stemmer.stem(w) for w in tokens       # stem words
#               if w not in stop_words]               # remove stopwords
#     return ' '.join(tokens)

# # Apply preprocessing (takes 1-2 minutes on 44k articles)
# print("Preprocessing... please wait")
# df['cleaned'] = df['content'].apply(preprocess)

# print("Done! Sample output:")
# print(df['cleaned'].iloc[0][:200])

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import PassiveAggressiveClassifier
# from sklearn.metrics import accuracy_score, classification_report
# import joblib

# # Step 3 — TF-IDF Feature Extraction
# print("Extracting features...")

# X = df['cleaned']
# y = df['label']

# # Split data: 80% train, 20% test
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y
# )

# # Convert text to numbers using TF-IDF
# vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
# X_train_tfidf = vectorizer.fit_transform(X_train)
# X_test_tfidf  = vectorizer.transform(X_test)

# print("Train shape:", X_train_tfidf.shape)
# print("Test shape: ", X_test_tfidf.shape)

# # Step 4 — Train the Model
# print("\nTraining model...")

# model = PassiveAggressiveClassifier(max_iter=50)
# model.fit(X_train_tfidf, y_train)

# # Evaluate
# y_pred = model.predict(X_test_tfidf)
# acc = accuracy_score(y_test, y_pred)

# print(f"\nAccuracy: {acc * 100:.2f}%")
# print("\nDetailed Report:")
# print(classification_report(y_test, y_pred, target_names=['Real', 'Fake']))

# # Step 5 — Save the model
# joblib.dump(model, 'fake_news_model.pkl')
# joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
# print("\nModel saved successfully!")

import pandas as pd
import re
import joblib
import nltk
import spacy
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, PassiveAggressiveClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MaxAbsScaler

nltk.download('stopwords')
nlp   = spacy.load('en_core_web_sm')
stops = set(stopwords.words('english'))

# ── Step 1: Load ───────────────────────────────────────────
df = pd.read_csv('train.csv').fillna('')
df['content'] = df['title'] + ' ' + df['text']
print("Loaded:", len(df), "articles")

# ── Step 2: Preprocess with spaCy ─────────────────────────
def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    doc  = nlp(text, disable=['parser', 'ner'])
    tokens = [token.lemma_ for token in doc
              if token.text not in stops and not token.is_punct]
    return ' '.join(tokens)

print("Preprocessing with spaCy... (takes 3-5 mins)")
df['cleaned'] = df['content'].apply(preprocess)
print("Preprocessing done!")

# ── Step 3: Split ──────────────────────────────────────────
X = df['cleaned']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ── Step 4: TF-IDF ────────────────────────────────────────
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf  = vectorizer.transform(X_test)

# Scale for Naive Bayes (needs non-negative values)
scaler        = MaxAbsScaler()
X_train_scaled = scaler.fit_transform(X_train_tfidf)
X_test_scaled  = scaler.transform(X_test_tfidf)

# ── Step 5: Train baseline (NLTK only, no spaCy) ──────────
# This simulates the "before" F1 score for your resume
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

def preprocess_basic(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [stemmer.stem(w) for w in tokens if w not in stops]
    return ' '.join(tokens)

print("Computing baseline F1 score...")
X_basic = df['content'].apply(preprocess_basic)
X_tr_b, X_te_b, y_tr_b, y_te_b = train_test_split(
    X_basic, y, test_size=0.2, random_state=42, stratify=y
)
vec_basic = TfidfVectorizer(max_features=5000)
Xb_train  = vec_basic.fit_transform(X_tr_b)
Xb_test   = vec_basic.transform(X_te_b)
baseline  = PassiveAggressiveClassifier(max_iter=50)
baseline.fit(Xb_train, y_tr_b)
f1_before = f1_score(y_te_b, baseline.predict(Xb_test))
print(f"Baseline F1 (stemming only): {f1_before:.2f}")

# ── Step 6: Ensemble Model ────────────────────────────────
print("\nTraining ensemble model...")

lr  = LogisticRegression(max_iter=1000, C=1.0)
nb  = MultinomialNB(alpha=0.1)
pac = PassiveAggressiveClassifier(max_iter=50)

# Train each individually on scaled data
lr.fit(X_train_scaled, y_train)
nb.fit(X_train_scaled, y_train)
pac.fit(X_train_scaled, y_train)

# Voting ensemble
ensemble = VotingClassifier(
    estimators=[('lr', lr), ('nb', nb), ('pac', pac)],
    voting='hard'
)
ensemble.fit(X_train_scaled, y_train)

# ── Step 7: Evaluate ──────────────────────────────────────
y_pred = ensemble.predict(X_test_scaled)
acc    = accuracy_score(y_test, y_pred)
f1     = f1_score(y_test, y_pred)

print(f"\nEnsemble Accuracy : {acc * 100:.2f}%")
print(f"F1 before spaCy   : {f1_before:.2f}")
print(f"F1 after spaCy    : {f1:.2f}")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred, target_names=['Real', 'Fake']))

# ── Step 8: Save ──────────────────────────────────────────
joblib.dump(ensemble, 'fake_news_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("\nAll models saved!")


