from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Shape Match Game</title>

  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #eef2ff, #fdf2f8);
      min-height: 100vh;
      color: #1e293b;
    }

    .container {
      max-width: 1100px;
      margin: 0 auto;
      padding: 32px 20px;
      text-align: center;
    }

    h1 {
      font-size: 42px;
      margin-bottom: 8px;
      color: #312e81;
    }

    .subtitle {
      font-size: 18px;
      color: #64748b;
      margin-bottom: 30px;
    }

    .message {
      min-height: 48px;
      font-size: 28px;
      font-weight: bold;
      color: #16a34a;
      margin-bottom: 20px;
    }

    .targets {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-bottom: 40px;
    }

    .target {
      height: 130px;
      border: 3px dashed #94a3b8;
      border-radius: 22px;
      background: rgba(255,255,255,0.8);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 52px;
      transition: 0.2s;
    }

    .target span {
      opacity: 0.25;
    }

    .target.hover {
      transform: scale(1.04);
      border-color: #6366f1;
      background: #eef2ff;
    }

    .target.correct {
      border-style: solid;
      border-color: #22c55e;
      background: #dcfce7;
    }

    .shapes {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 18px;
      padding: 24px;
      border-radius: 26px;
      background: white;
      box-shadow: 0 18px 50px rgba(15, 23, 42, 0.12);
    }

    .shape {
      width: 95px;
      height: 95px;
      border-radius: 20px;
      background: #f8fafc;
      border: 2px solid #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 48px;
      cursor: grab;
      user-select: none;
      transition: 0.2s;
    }

    .shape:hover {
      transform: translateY(-4px);
      box-shadow: 0 10px 24px rgba(15, 23, 42, 0.15);
    }

    .shape:active {
      cursor: grabbing;
    }

    .shape.hidden {
      visibility: hidden;
    }

    .reset-btn {
      margin-top: 28px;
      padding: 14px 26px;
      border: none;
      border-radius: 14px;
      background: #4f46e5;
      color: white;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
    }

    .reset-btn:hover {
      background: #4338ca;
    }

    @media (max-width: 800px) {
      .targets {
        grid-template-columns: repeat(2, 1fr);
      }

      h1 {
        font-size: 32px;
      }
    }
  </style>
</head>

<body>
  <div class="container">
    <h1>Şekil Eşleştirme Oyunu 🎨</h1>
    <p class="subtitle">Şekilleri doğru kutulara sürükle ve eşleştir.</p>

    <div id="message" class="message"></div>

    <div class="targets">
      <div class="target" data-shape="circle"><span>⚪</span></div>
      <div class="target" data-shape="square"><span>⬜</span></div>
      <div class="target" data-shape="triangle"><span>🔺</span></div>
      <div class="target" data-shape="star"><span>⭐</span></div>
      <div class="target" data-shape="heart"><span>❤️</span></div>
      <div class="target" data-shape="diamond"><span>🔷</span></div>
      <div class="target" data-shape="moon"><span>🌙</span></div>
      <div class="target" data-shape="sun"><span>☀️</span></div>
    </div>

    <div class="shapes">
      <div class="shape" draggable="true" data-shape="sun">☀️</div>
      <div class="shape" draggable="true" data-shape="heart">❤️</div>
      <div class="shape" draggable="true" data-shape="square">⬜</div>
      <div class="shape" draggable="true" data-shape="moon">🌙</div>
      <div class="shape" draggable="true" data-shape="triangle">🔺</div>
      <div class="shape" draggable="true" data-shape="diamond">🔷</div>
      <div class="shape" draggable="true" data-shape="circle">⚪</div>
      <div class="shape" draggable="true" data-shape="star">⭐</div>
    </div>

    <button class="reset-btn" onclick="location.reload()">Yeniden Başlat</button>
  </div>

  <script>
    let draggedShape = null;
    let correctCount = 0;
    const totalShapes = 8;

    const shapes = document.querySelectorAll(".shape");
    const targets = document.querySelectorAll(".target");
    const message = document.getElementById("message");

    shapes.forEach(shape => {
      shape.addEventListener("dragstart", () => {
        draggedShape = shape;
      });
    });

    targets.forEach(target => {
      target.addEventListener("dragover", event => {
        event.preventDefault();
        target.classList.add("hover");
      });

      target.addEventListener("dragleave", () => {
        target.classList.remove("hover");
      });

      target.addEventListener("drop", event => {
        event.preventDefault();
        target.classList.remove("hover");

        if (!draggedShape || target.classList.contains("correct")) {
          return;
        }

        const targetShape = target.dataset.shape;
        const draggedShapeName = draggedShape.dataset.shape;

        if (targetShape === draggedShapeName) {
          target.innerHTML = draggedShape.innerHTML;
          target.classList.add("correct");
          draggedShape.classList.add("hidden");
          correctCount++;

          if (correctCount === totalShapes) {
            message.innerHTML = "Success 🎉 Tüm şekiller doğru eşleşti!";
          }
        } else {
          message.innerHTML = "Tekrar dene 🙂";
          setTimeout(() => {
            if (correctCount !== totalShapes) {
              message.innerHTML = "";
            }
          }, 1000);
        }
      });
    });
  </script>
</body>
</html>
"""

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
