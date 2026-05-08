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
    * { box-sizing: border-box; }

    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #eef2ff, #fdf2f8);
      min-height: 100vh;
      color: #1e293b;
    }

    .container {
      max-width: 1150px;
      margin: 0 auto;
      padding: 30px 20px;
      text-align: center;
    }

    h1 {
      font-size: 40px;
      margin-bottom: 8px;
      color: #312e81;
    }

    .subtitle {
      font-size: 18px;
      color: #64748b;
      margin-bottom: 18px;
    }

    .topbar {
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 22px;
    }

    .badge {
      background: white;
      border-radius: 16px;
      padding: 12px 18px;
      font-weight: bold;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.10);
    }

    .message {
      min-height: 48px;
      font-size: 26px;
      font-weight: bold;
      color: #16a34a;
      margin-bottom: 18px;
    }

    .targets {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 34px;
    }

    .target {
      height: 125px;
      border: 3px dashed #94a3b8;
      border-radius: 22px;
      background: rgba(255,255,255,0.82);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 52px;
      transition: 0.2s;
    }

    .target span {
      opacity: 0.22;
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
      gap: 16px;
      padding: 24px;
      border-radius: 26px;
      background: white;
      box-shadow: 0 18px 50px rgba(15, 23, 42, 0.12);
    }

    .shape {
      width: 92px;
      height: 92px;
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

    .shape.selected {
      border-color: #4f46e5;
      background: #eef2ff;
      transform: scale(1.08);
    }

    .shape.hidden {
      visibility: hidden;
    }

    .actions {
      margin-top: 28px;
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    button {
      padding: 14px 24px;
      border: none;
      border-radius: 14px;
      color: white;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
    }

    .next-btn { background: #16a34a; display: none; }
    .reset-btn { background: #4f46e5; }

    button:hover { opacity: 0.9; }

    @media (max-width: 800px) {
      .targets { grid-template-columns: repeat(2, 1fr); }
      h1 { font-size: 30px; }
      .shape { width: 78px; height: 78px; font-size: 40px; }
    }
  </style>
</head>

<body>
  <div class="container">
    <h1>Şekil Eşleştirme Oyunu 🎨</h1>
    <p class="subtitle">Seviyeleri tamamla, şekilleri doğru kutulara sürükle veya dokunarak eşleştir.</p>

    <div class="topbar">
      <div class="badge" id="levelBadge">Level 1 / 10</div>
      <div class="badge" id="difficultyBadge">Zorluk: Kolay</div>
      <div class="badge" id="scoreBadge">Doğru: 0</div>
    </div>

    <div id="message" class="message"></div>

    <div id="targets" class="targets"></div>
    <div id="shapes" class="shapes"></div>

    <div class="actions">
      <button class="next-btn" id="nextBtn">Sonraki Level</button>
      <button class="reset-btn" onclick="restartGame()">Baştan Başlat</button>
    </div>
  </div>

  <script>
    const allShapes = [
      { id: "circle", icon: "⚪" },
      { id: "square", icon: "⬜" },
      { id: "triangle", icon: "🔺" },
      { id: "star", icon: "⭐" },
      { id: "heart", icon: "❤️" },
      { id: "diamond", icon: "🔷" },
      { id: "moon", icon: "🌙" },
      { id: "sun", icon: "☀️" }
    ];

    const levelConfig = [
      { count: 3, difficulty: "Çok Kolay" },
      { count: 3, difficulty: "Çok Kolay" },
      { count: 4, difficulty: "Kolay" },
      { count: 4, difficulty: "Kolay" },
      { count: 5, difficulty: "Orta" },
      { count: 5, difficulty: "Orta" },
      { count: 6, difficulty: "Zor" },
      { count: 6, difficulty: "Zor" },
      { count: 7, difficulty: "Çok Zor" },
      { count: 8, difficulty: "Usta" }
    ];

    let currentLevel = 0;
    let correctCount = 0;
    let draggedShape = null;

    const targetsEl = document.getElementById("targets");
    const shapesEl = document.getElementById("shapes");
    const messageEl = document.getElementById("message");
    const levelBadge = document.getElementById("levelBadge");
    const difficultyBadge = document.getElementById("difficultyBadge");
    const scoreBadge = document.getElementById("scoreBadge");
    const nextBtn = document.getElementById("nextBtn");

    function shuffle(array) {
      return [...array].sort(() => Math.random() - 0.5);
    }

    function handleMatch(target, config) {
      if (!draggedShape || target.classList.contains("correct")) {
        return;
      }

      if (target.dataset.shape === draggedShape.dataset.shape) {
        target.innerHTML = draggedShape.innerHTML;
        target.classList.add("correct");

        draggedShape.classList.add("hidden");
        draggedShape.classList.remove("selected");

        correctCount++;

        scoreBadge.innerHTML = `Doğru: ${correctCount} / ${config.count}`;

        if (correctCount === config.count) {
          if (currentLevel === 9) {
            messageEl.innerHTML = "Tebrikler! Tüm seviyeleri tamamladın 🎉";
            nextBtn.style.display = "none";
          } else {
            messageEl.innerHTML = "Success 🎉 Level tamamlandı!";
            nextBtn.style.display = "inline-block";
          }
        }
      } else {
        messageEl.innerHTML = "Tekrar dene 🙂";

        setTimeout(() => {
          if (correctCount !== config.count) {
            messageEl.innerHTML = "";
          }
        }, 900);
      }
    }

    function loadLevel() {
      correctCount = 0;
      draggedShape = null;
      messageEl.innerHTML = "";
      nextBtn.style.display = "none";

      const config = levelConfig[currentLevel];
      const selectedShapes = shuffle(allShapes).slice(0, config.count);
      const shuffledShapes = shuffle(selectedShapes);

      levelBadge.innerHTML = `Level ${currentLevel + 1} / 10`;
      difficultyBadge.innerHTML = `Zorluk: ${config.difficulty}`;
      scoreBadge.innerHTML = `Doğru: 0 / ${config.count}`;

      targetsEl.innerHTML = "";
      shapesEl.innerHTML = "";

      selectedShapes.forEach(shape => {
        const target = document.createElement("div");
        target.className = "target";
        target.dataset.shape = shape.id;
        target.innerHTML = `<span>${shape.icon}</span>`;

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
          handleMatch(target, config);
        });

        target.addEventListener("click", () => {
          handleMatch(target, config);
        });

        targetsEl.appendChild(target);
      });

      shuffledShapes.forEach(shape => {
        const shapeEl = document.createElement("div");
        shapeEl.className = "shape";
        shapeEl.draggable = true;
        shapeEl.dataset.shape = shape.id;
        shapeEl.innerHTML = shape.icon;

        shapeEl.addEventListener("dragstart", () => {
          draggedShape = shapeEl;
        });

        shapeEl.addEventListener("click", () => {
          document.querySelectorAll(".shape").forEach(s =>
            s.classList.remove("selected")
          );

          shapeEl.classList.add("selected");
          draggedShape = shapeEl;
        });

        shapesEl.appendChild(shapeEl);
      });
    }

    nextBtn.addEventListener("click", () => {
      if (currentLevel < 9) {
        currentLevel++;
        loadLevel();
      }
    });

    function restartGame() {
      currentLevel = 0;
      loadLevel();
    }

    loadLevel();
  </script>
</body>
</html>
"""

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
