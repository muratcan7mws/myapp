from flask import Flask

app = Flask(__name__)

# Ana endpoint
@app.route("/")
def home():
    return "Seni çok seviyorum Duyguu7 <3 🚀"

# Health check endpoint (CI/CD için kritik)
@app.route("/health")
def health():
    return "OK", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
