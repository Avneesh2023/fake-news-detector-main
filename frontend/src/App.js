import { useState } from "react";
import "./App.css";

function App() {
  const [article, setArticle] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const wordCount = article.trim() === "" ? 0 : article.trim().split(/\s+/).length;
  const charCount = article.length;

  const analyse = async () => {
    if (!article.trim()) return;
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      const res = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: article }),
      });
      const data = await res.json();
      if (res.ok) {
        setResult(data);
      } else {
        setError(data.error || "An error occurred");
      }
    } catch (err) {
      setError("Could not connect to server. Make sure Flask is running on port 5000.");
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <div className="header">
        <h1 className="title">VeriFact</h1>
        <p className="subtitle">AI-Powered Fake News Detection</p>
      </div>

      <div className="input-section">
        <textarea
          className="textarea"
          placeholder="Paste the news article text here to verify its authenticity..."
          value={article}
          onChange={(e) => setArticle(e.target.value)}
        />
        <div className="stats">
          <span>{charCount} characters</span>
          <span>&bull;</span>
          <span>{wordCount} words</span>
        </div>
      </div>

      <button
        className="analyze-btn"
        onClick={analyse}
        disabled={loading || article.trim().length === 0}
      >
        {loading ? (
          <>
            <span className="loader-spinner"></span> Analyzing...
          </>
        ) : (
          "Verify Authenticity"
        )}
      </button>

      {error && <div className="error-message">{error}</div>}

      {result && (
        <div className="results-section">
          <div className={`prediction-card ${result.result === "FAKE" ? "fake" : "real"}`}>
            <span className="prediction-icon">
              {result.result === "FAKE" ? "⚠️" : "✅"}
            </span>
            <p className="prediction-text">
              {result.result === "FAKE"
                ? "High Probability of Fake News"
                : "Appears to be Authentic News"}
            </p>
          </div>

          <div className="confidence-box">
            <div className="conf-header">
              <span>AI Confidence Level</span>
              <span className="conf-value">{result.confidence}%</span>
            </div>
            <div className="conf-track">
              <div
                className="conf-fill"
                style={{
                  width: `${result.confidence}%`,
                  backgroundColor: result.result === "FAKE" ? "#ef4444" : "#22c55e",
                  color: result.result === "FAKE" ? "#ef4444" : "#22c55e"
                }}
              />
            </div>
          </div>

          <div className="votes-box">
            <h3 className="votes-title">Individual Model Analysis</h3>
            {Object.entries(result.votes).map(([model, vote]) => (
              <div key={model} className="vote-row">
                <span className="model-name">{model.replace(/_/g, " ")}</span>
                <span className={`badge ${vote === "FAKE" ? "fake" : "real"}`}>
                  {vote}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;