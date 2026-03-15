 import { useState } from "react";

function App() {
  const [article, setArticle] = useState("");
  const [result, setResult]   = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError]     = useState(null);

  const wordCount = article.trim() === "" ? 0 : article.trim().split(/\s+/).length;
  const charCount = article.length;

  const analyse = async () => {
    if (!article.trim()) return;
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      const res  = await fetch("http://localhost:5000/predict", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ text: article }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError("Could not connect to server. Make sure Flask is running.");
    }
    setLoading(false);
  };

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.title}>Fake News Detector</h1>
        <p style={styles.subtitle}>
          Paste any news article to check if it's real or fake.
        </p>

        <textarea
          style={styles.textarea}
          rows={8}
          placeholder="Paste your news article here..."
          value={article}
          onChange={(e) => setArticle(e.target.value)}
        />

        <div style={styles.counter}>
          {charCount} characters &nbsp;|&nbsp; {wordCount} words
        </div>

        <button
          style={{ ...styles.button, opacity: loading ? 0.7 : 1 }}
          onClick={analyse}
          disabled={loading}
        >
          {loading ? "Analysing..." : "Analyse"}
        </button>

        {error && <div style={styles.error}>{error}</div>}

        {result && (
          <>
            <div style={result.result === "FAKE" ? styles.fake : styles.real}>
              {result.result === "FAKE"
                ? "This article is likely FAKE"
                : "This article appears to be REAL"}
            </div>

            <div style={styles.confBox}>
              <div style={styles.confHeader}>
                <span>Confidence</span>
                <strong>{result.confidence}%</strong>
              </div>
              <div style={styles.confTrack}>
                <div style={{
                  ...styles.confFill,
                  width: `${result.confidence}%`,
                  background: result.result === "FAKE" ? "#e74c3c" : "#2ecc71"
                }}/>
              </div>
            </div>

            <div style={styles.votesBox}>
              <p style={styles.votesTitle}>Individual model votes:</p>
              {Object.entries(result.votes).map(([model, vote]) => (
                <div key={model} style={styles.voteRow}>
                  <span style={styles.modelName}>
                    {model.replace(/_/g, " ")}
                  </span>
                  <span style={vote === "FAKE" ? styles.fakeBadge : styles.realBadge}>
                    {vote}
                  </span>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}

const styles = {
  page:       { minHeight: "100vh", background: "#f0f2f5", display: "flex", justifyContent: "center", alignItems: "flex-start", padding: "40px 16px", fontFamily: "'Segoe UI', sans-serif" },
  card:       { background: "#fff", borderRadius: "12px", padding: "36px", maxWidth: "680px", width: "100%", boxShadow: "0 4px 20px rgba(0,0,0,0.08)" },
  title:      { fontSize: "26px", marginBottom: "8px", color: "#1a1a2e" },
  subtitle:   { color: "#666", marginBottom: "24px", fontSize: "15px" },
  textarea:   { width: "100%", border: "1.5px solid #ddd", borderRadius: "8px", padding: "14px", fontSize: "15px", resize: "vertical", outline: "none", boxSizing: "border-box", fontFamily: "'Segoe UI', sans-serif" },
  counter:    { textAlign: "right", fontSize: "13px", color: "#999", marginTop: "6px" },
  button:     { marginTop: "14px", width: "100%", padding: "13px", background: "#4361ee", color: "#fff", border: "none", borderRadius: "8px", fontSize: "16px", cursor: "pointer" },
  error:      { marginTop: "16px", padding: "14px", background: "#fff3cd", borderRadius: "8px", color: "#856404", fontSize: "14px" },
  fake:       { marginTop: "24px", padding: "18px", background: "#fff0f0", color: "#c0392b", border: "1.5px solid #f5c6cb", borderRadius: "8px", fontSize: "17px", textAlign: "center" },
  real:       { marginTop: "24px", padding: "18px", background: "#f0fff4", color: "#1a7a4a", border: "1.5px solid #b2dfdb", borderRadius: "8px", fontSize: "17px", textAlign: "center" },
  confBox:    { marginTop: "16px", padding: "16px", border: "1.5px solid #eee", borderRadius: "8px" },
  confHeader: { display: "flex", justifyContent: "space-between", fontSize: "14px", marginBottom: "10px" },
  confTrack:  { background: "#eee", borderRadius: "99px", height: "10px", overflow: "hidden" },
  confFill:   { height: "100%", borderRadius: "99px", transition: "width 0.6s ease" },
  votesBox:   { marginTop: "16px", padding: "16px", background: "#f8f9fa", borderRadius: "8px" },
  votesTitle: { fontSize: "13px", color: "#666", marginBottom: "10px" },
  voteRow:    { display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "8px" },
  modelName:  { fontSize: "13px", color: "#444", textTransform: "capitalize" },
  fakeBadge:  { fontSize: "12px", padding: "3px 10px", background: "#fff0f0", color: "#c0392b", borderRadius: "99px", border: "1px solid #f5c6cb" },
  realBadge:  { fontSize: "12px", padding: "3px 10px", background: "#f0fff4", color: "#1a7a4a", borderRadius: "99px", border: "1px solid #b2dfdb" },
};

export default App;