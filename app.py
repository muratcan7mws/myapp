from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfa
@app.route("/")
def home():
    return render_template("index.html")

# Health check
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
