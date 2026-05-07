from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>MWS7 Lab</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: #0f172a;
      color: white;
    }
    .hero {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 40px;
    }
    .card {
      max-width: 760px;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 24px;
      padding: 48px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.35);
    }
    h1 {
      font-size: 56px;
      margin-bottom: 16px;
    }
    p {
      font-size: 20px;
      color: #cbd5e1;
      line-height: 1.6;
    }
    .buttons {
      margin-top: 32px;
    }
    a {
      display: inline-block;
      margin: 8px;
      padding: 14px 24px;
      border-radius: 12px;
      text-decoration: none;
      font-weight: bold;
    }
    .primary {
      background: #38bdf8;
      color: #020617;
    }
    .secondary {
      border: 1px solid #38bdf8;
      color: #38bdf8;
    }
  </style>
</head>
<body>
  <section class="hero">
    <div class="card">
      <h1>MWS7 Tech 🚀</h1>
      <p>
        DevOps, SRE, CI/CD, Docker, Jenkins ve Nginx reverse proxy üzerine
        kurulu kişisel teknoloji lab ortamım.
      </p>
      <div class="buttons">
        <a class="primary" href="https://app.mws7.tech">Projeleri Gör</a>
        <a class="secondary" href="https://jenkins.mws7.tech">Jenkins Paneli</a>
      </div>
    </div>
  </section>
</body>
</html>
"""

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
