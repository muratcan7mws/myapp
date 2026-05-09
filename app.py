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
  <title>Çocuk Oyunları</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #eef2ff, #fdf2f8);
      color: #1e293b;
    }

    .container {
      max-width: 1100px;
      margin: auto;
      padding: 28px 18px;
      text-align: center;
    }

    h1 {
      color: #312e81;
      font-size: 42px;
    }

    .menu {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 18px;
      margin-top: 30px;
    }

    .card {
      background: white;
      border-radius: 24px;
      padding: 28px 18px;
      box-shadow: 0 14px 40px rgba(15,23,42,.12);
      cursor: pointer;
      transition: .2s;
    }

    .card:hover {
      transform: translateY(-6px);
    }

    .icon {
      font-size: 54px;
      margin-bottom: 12px;
    }

    .game {
      display: none;
      background: white;
      margin-top: 24px;
      border-radius: 26px;
      padding: 26px;
      box-shadow: 0 14px 40px rgba(15,23,42,.12);
    }

    button {
      border: none;
      border-radius: 14px;
      padding: 13px 22px;
      background: #4f46e5;
      color: white;
      font-weight: bold;
      cursor: pointer;
      margin: 8px;
    }

    .back {
      background: #64748b;
    }

    .success {
      color: #16a34a;
      font-size: 26px;
      font-weight: bold;
      min-height: 36px;
    }

    .items {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 14px;
      margin-top: 20px;
    }

    .box, .choice {
      width: 95px;
      height: 95px;
      border-radius: 20px;
      background: #f8fafc;
      border: 2px solid #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 44px;
      cursor: pointer;
    }

    .selected {
      border-color: #4f46e5;
      background: #eef2ff;
      transform: scale(1.06);
    }

    .correct {
      background: #dcfce7;
      border-color: #22c55e;
    }

    .hidden {
      visibility: hidden;
    }

    input {
      padding: 14px;
      border-radius: 12px;
      border: 1px solid #cbd5e1;
      font-size: 18px;
      text-align: center;
    }

    @media(max-width: 700px) {
      h1 { font-size: 30px; }
      .box, .choice {
        width: 76px;
        height: 76px;
        font-size: 36px;
      }
    }
  </style>
</head>

<body>
  <div class="container">
    <h1>Çocuk Oyunları 🎈</h1>
    <p>Oynamak istediğin oyunu seç.</p>

    <div id="menu" class="menu">
      <div class="card" onclick="openGame('shapeGame')">
        <div class="icon">🔺</div>
        <h3>Şekil Eşleştirme</h3>
        <p>Şekilleri doğru kutuya koy.</p>
      </div>

      <div class="card" onclick="openGame('colorGame')">
        <div class="icon">🎨</div>
        <h3>Renk Eşleştirme</h3>
        <p>Renkleri doğru isimle eşleştir.</p>
      </div>

      <div class="card" onclick="openGame('numberGame')">
        <div class="icon">🔢</div>
        <h3>Sayı Oyunu</h3>
        <p>Kaç tane nesne var?</p>
      </div>

      <div class="card" onclick="openGame('memoryGame')">
        <div class="icon">🧠</div>
        <h3>Hafıza Oyunu</h3>
        <p>Aynı kartları bul.</p>
      </div>

      <div class="card" onclick="openGame('animalGame')">
        <div class="icon">🐶</div>
        <h3>Hayvan Eşleştirme</h3>
        <p>Hayvanı adıyla eşleştir.</p>
      </div>
    </div>

    <div id="shapeGame" class="game">
      <h2>Şekil Eşleştirme 🔺</h2>
      <div id="shapeMsg" class="success"></div>
      <div class="items" id="shapeTargets"></div>
      <div class="items" id="shapeChoices"></div>
      <button class="back" onclick="goHome()">Ana Menü</button>
    </div>

    <div id="colorGame" class="game">
      <h2>Renk Eşleştirme 🎨</h2>
      <div id="colorMsg" class="success"></div>
      <div class="items" id="colorTargets"></div>
      <div class="items" id="colorChoices"></div>
      <button class="back" onclick="goHome()">Ana Menü</button>
    </div>

    <div id="numberGame" class="game">
      <h2>Sayı Oyunu 🔢</h2>
      <div id="numberQuestion" style="font-size:52px;margin:20px;"></div>
      <input id="numberAnswer" type="number" placeholder="Kaç tane?" />
      <br>
      <button onclick="checkNumber()">Kontrol Et</button>
      <div id="numberMsg" class="success"></div>
      <button class="back" onclick="goHome()">Ana Menü</button>
    </div>

    <div id="memoryGame" class="game">
      <h2>Hafıza Oyunu 🧠</h2>
      <div id="memoryMsg" class="success"></div>
      <div class="items" id="memoryBoard"></div>
      <button class="back" onclick="goHome()">Ana Menü</button>
    </div>

    <div id="animalGame" class="game">
      <h2>Hayvan Eşleştirme 🐶</h2>
      <div id="animalMsg" class="success"></div>
      <div class="items" id="animalTargets"></div>
      <div class="items" id="animalChoices"></div>
      <button class="back" onclick="goHome()">Ana Menü</button>
    </div>
  </div>

<script>
function hideAll() {
  document.getElementById("menu").style.display = "none";
  document.querySelectorAll(".game").forEach(g => g.style.display = "none");
}

function openGame(id) {
  hideAll();
  document.getElementById(id).style.display = "block";

  if (id === "shapeGame") loadShapeGame();
  if (id === "colorGame") loadColorGame();
  if (id === "numberGame") loadNumberGame();
  if (id === "memoryGame") loadMemoryGame();
  if (id === "animalGame") loadAnimalGame();
}

function goHome() {
  document.querySelectorAll(".game").forEach(g => g.style.display = "none");
  document.getElementById("menu").style.display = "grid";
}

function shuffle(arr) {
  return [...arr].sort(() => Math.random() - 0.5);
}

/* 1 - ŞEKİL OYUNU */
const shapes = [
  {id:"circle", icon:"⚪"},
  {id:"square", icon:"⬜"},
  {id:"triangle", icon:"🔺"},
  {id:"star", icon:"⭐"},
  {id:"heart", icon:"❤️"}
];

let selectedShape = null;
let shapeCorrect = 0;

function loadShapeGame() {
  selectedShape = null;
  shapeCorrect = 0;
  shapeMsg.innerHTML = "";
  shapeTargets.innerHTML = "";
  shapeChoices.innerHTML = "";

  shapes.forEach(s => {
    let t = document.createElement("div");
    t.className = "box";
    t.dataset.id = s.id;
    t.innerHTML = "❔";
    t.onclick = () => matchShape(t);
    shapeTargets.appendChild(t);
  });

  shuffle(shapes).forEach(s => {
    let c = document.createElement("div");
    c.className = "choice";
    c.dataset.id = s.id;
    c.innerHTML = s.icon;
    c.onclick = () => {
      document.querySelectorAll("#shapeChoices .choice").forEach(x => x.classList.remove("selected"));
      c.classList.add("selected");
      selectedShape = c;
    };
    shapeChoices.appendChild(c);
  });
}

function matchShape(target) {
  if (!selectedShape || target.classList.contains("correct")) return;

  if (selectedShape.dataset.id === target.dataset.id) {
    target.innerHTML = selectedShape.innerHTML;
    target.classList.add("correct");
    selectedShape.classList.add("hidden");
    shapeCorrect++;

    if (shapeCorrect === shapes.length) {
      shapeMsg.innerHTML = "Success 🎉";
    }
  }
}

/* 2 - RENK OYUNU */
const colors = [
  {id:"red", name:"Kırmızı", color:"#ef4444"},
  {id:"blue", name:"Mavi", color:"#3b82f6"},
  {id:"green", name:"Yeşil", color:"#22c55e"},
  {id:"yellow", name:"Sarı", color:"#eab308"}
];

let selectedColor = null;
let colorCorrect = 0;

function loadColorGame() {
  selectedColor = null;
  colorCorrect = 0;
  colorMsg.innerHTML = "";
  colorTargets.innerHTML = "";
  colorChoices.innerHTML = "";

  colors.forEach(c => {
    let t = document.createElement("div");
    t.className = "box";
    t.dataset.id = c.id;
    t.style.fontSize = "20px";
    t.innerHTML = c.name;
    t.onclick = () => matchColor(t);
    colorTargets.appendChild(t);
  });

  shuffle(colors).forEach(c => {
    let ch = document.createElement("div");
    ch.className = "choice";
    ch.dataset.id = c.id;
    ch.style.background = c.color;
    ch.onclick = () => {
      document.querySelectorAll("#colorChoices .choice").forEach(x => x.classList.remove("selected"));
      ch.classList.add("selected");
      selectedColor = ch;
    };
    colorChoices.appendChild(ch);
  });
}

function matchColor(target) {
  if (!selectedColor || target.classList.contains("correct")) return;

  if (selectedColor.dataset.id === target.dataset.id) {
    target.classList.add("correct");
    selectedColor.classList.add("hidden");
    colorCorrect++;

    if (colorCorrect === colors.length) {
      colorMsg.innerHTML = "Success 🎉";
    }
  }
}

/* 3 - SAYI OYUNU */
let currentNumber = 0;

function loadNumberGame() {
  currentNumber = Math.floor(Math.random() * 5) + 3;
  numberQuestion.innerHTML = "🍎 ".repeat(currentNumber);
  numberAnswer.value = "";
  numberMsg.innerHTML = "";
}

function checkNumber() {
  if (Number(numberAnswer.value) === currentNumber) {
    numberMsg.innerHTML = "Success 🎉 Doğru bildin!";
  } else {
    numberMsg.innerHTML = "Tekrar dene 🙂";
  }
}

/* 4 - HAFIZA OYUNU */
let memoryFirst = null;
let memoryLock = false;
let memoryFound = 0;

function loadMemoryGame() {
  memoryFirst = null;
  memoryLock = false;
  memoryFound = 0;
  memoryMsg.innerHTML = "";
  memoryBoard.innerHTML = "";

  const cards = shuffle(["🐶","🐱","🐰","🦊","🐶","🐱","🐰","🦊"]);

  cards.forEach(icon => {
    let card = document.createElement("div");
    card.className = "box";
    card.dataset.icon = icon;
    card.innerHTML = "❓";
    card.onclick = () => flipCard(card);
    memoryBoard.appendChild(card);
  });
}

function flipCard(card) {
  if (memoryLock || card.classList.contains("correct") || card === memoryFirst) return;

  card.innerHTML = card.dataset.icon;

  if (!memoryFirst) {
    memoryFirst = card;
  } else {
    if (memoryFirst.dataset.icon === card.dataset.icon) {
      memoryFirst.classList.add("correct");
      card.classList.add("correct");
      memoryFound++;
      memoryFirst = null;

      if (memoryFound === 4) {
        memoryMsg.innerHTML = "Success 🎉";
      }
    } else {
      memoryLock = true;
      setTimeout(() => {
        memoryFirst.innerHTML = "❓";
        card.innerHTML = "❓";
        memoryFirst = null;
        memoryLock = false;
      }, 700);
    }
  }
}

/* 5 - HAYVAN OYUNU */
const animals = [
  {id:"dog", icon:"🐶", name:"Köpek"},
  {id:"cat", icon:"🐱", name:"Kedi"},
  {id:"rabbit", icon:"🐰", name:"Tavşan"},
  {id:"lion", icon:"🦁", name:"Aslan"}
];

let selectedAnimal = null;
let animalCorrect = 0;

function loadAnimalGame() {
  selectedAnimal = null;
  animalCorrect = 0;
  animalMsg.innerHTML = "";
  animalTargets.innerHTML = "";
  animalChoices.innerHTML = "";

  animals.forEach(a => {
    let t = document.createElement("div");
    t.className = "box";
    t.dataset.id = a.id;
    t.style.fontSize = "20px";
    t.innerHTML = a.name;
    t.onclick = () => matchAnimal(t);
    animalTargets.appendChild(t);
  });

  shuffle(animals).forEach(a => {
    let ch = document.createElement("div");
    ch.className = "choice";
    ch.dataset.id = a.id;
    ch.innerHTML = a.icon;
    ch.onclick = () => {
      document.querySelectorAll("#animalChoices .choice").forEach(x => x.classList.remove("selected"));
      ch.classList.add("selected");
      selectedAnimal = ch;
    };
    animalChoices.appendChild(ch);
  });
}

function matchAnimal(target) {
  if (!selectedAnimal || target.classList.contains("correct")) return;

  if (selectedAnimal.dataset.id === target.dataset.id) {
    target.classList.add("correct");
    selectedAnimal.classList.add("hidden");
    animalCorrect++;

    if (animalCorrect === animals.length) {
      animalMsg.innerHTML = "Success 🎉";
    }
  }
}
</script>
</body>
</html>
"""

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
