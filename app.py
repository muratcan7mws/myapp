from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Çocuk Oyunları</title>

<style>
body {
  margin:0;
  font-family:Arial,sans-serif;
  background:linear-gradient(135deg,#eef2ff,#fdf2f8);
  color:#1e293b;
}
.container {
  max-width:1300px;
  margin:auto;
  padding:24px;
}
h1,h2 { color:#312e81; text-align:center; }
.layout {
  display:grid;
  grid-template-columns:1fr 280px;
  gap:20px;
}
.menu {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
  gap:18px;
}
.card,.panel,.game {
  background:white;
  border-radius:24px;
  padding:22px;
  box-shadow:0 14px 40px rgba(15,23,42,.12);
}
.card {
  cursor:pointer;
  text-align:center;
  transition:.2s;
}
.card:hover { transform:translateY(-5px); }
.icon { font-size:52px; }
.game { display:none; text-align:center; }
.items {
  display:flex;
  flex-wrap:wrap;
  justify-content:center;
  gap:14px;
  margin-top:20px;
}
.box,.choice {
  width:90px;
  height:90px;
  border-radius:20px;
  border:2px solid #cbd5e1;
  background:#f8fafc;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:42px;
  cursor:pointer;
  user-select:none;
}
.choice.selected {
  border-color:#4f46e5;
  background:#eef2ff;
  transform:scale(1.07);
}
.correct {
  background:#dcfce7;
  border-color:#22c55e;
}
.hidden { visibility:hidden; }
button {
  border:none;
  border-radius:14px;
  padding:13px 22px;
  background:#4f46e5;
  color:white;
  font-weight:bold;
  cursor:pointer;
  margin:8px;
}
.back { background:#64748b; }
.success { color:#16a34a; font-size:24px; font-weight:bold; min-height:34px; }
.fail { color:#dc2626; font-size:22px; font-weight:bold; min-height:34px; }
.badge {
  display:inline-block;
  background:#eef2ff;
  padding:10px 14px;
  border-radius:14px;
  margin:6px;
  font-weight:bold;
}
.score-table {
  font-size:14px;
  max-height:520px;
  overflow:auto;
}
.row {
  display:flex;
  justify-content:space-between;
  border-bottom:1px solid #e2e8f0;
  padding:8px 0;
}
input {
  padding:14px;
  border-radius:12px;
  border:1px solid #cbd5e1;
  font-size:20px;
  text-align:center;
}
@media(max-width:900px){
  .layout { grid-template-columns:1fr; }
  .box,.choice { width:74px;height:74px;font-size:34px; }
}
</style>
</head>

<body>
<div class="container">
<h1>Çocuk Oyunları 🎈</h1>

<div class="layout">
  <main>
    <div id="menu" class="menu"></div>

    <div id="gameArea" class="game">
      <h2 id="gameTitle"></h2>
      <div>
        <span class="badge" id="levelBadge"></span>
        <span class="badge" id="scoreBadge"></span>
        <span class="badge" id="attemptBadge"></span>
      </div>

      <div id="message" class="success"></div>
      <div id="failMessage" class="fail"></div>

      <div id="questionArea"></div>
      <div class="items" id="targets"></div>
      <div class="items" id="choices"></div>

      <button class="back" onclick="goHome()">Ana Menü</button>
    </div>
  </main>

  <aside class="panel">
    <h3>Puan Tablosu 🏆</h3>
    <div>Toplam Puan: <b id="totalScore">0</b></div>
    <div>Deneme: <b id="attemptCount">0</b></div>
    <hr>
    <div id="scoreTable" class="score-table"></div>
  </aside>
</div>
</div>

<script>
const games = [
  {id:"shape", title:"Şekil Eşleştirme", icon:"🔺"},
  {id:"color", title:"Renk Eşleştirme", icon:"🎨"},
  {id:"number", title:"Sayı Oyunu", icon:"🔢"},
  {id:"memory", title:"Hafıza Oyunu", icon:"🧠"},
  {id:"animal", title:"Hayvan Eşleştirme", icon:"🐶"},
  {id:"letter", title:"Harf Oyunu", icon:"🔤"},
  {id:"pattern", title:"Sıralama Oyunu", icon:"🧩"},
  {id:"compare", title:"Büyük-Küçük Oyunu", icon:"⚖️"}
];

const shapes = [
  ["circle","⚪"],["square","⬜"],["triangle","🔺"],["star","⭐"],["heart","❤️"],
  ["diamond","🔷"],["moon","🌙"],["sun","☀️"],["cloud","☁️"],["flower","🌸"]
];

const colors = [
  ["red","Kırmızı","#ef4444"],["blue","Mavi","#3b82f6"],["green","Yeşil","#22c55e"],
  ["yellow","Sarı","#eab308"],["purple","Mor","#a855f7"],["orange","Turuncu","#f97316"],
  ["pink","Pembe","#ec4899"],["black","Siyah","#111827"]
];

const animals = [
  ["dog","🐶","Köpek"],["cat","🐱","Kedi"],["rabbit","🐰","Tavşan"],["lion","🦁","Aslan"],
  ["fish","🐟","Balık"],["bird","🐦","Kuş"],["cow","🐮","İnek"],["monkey","🐵","Maymun"]
];

const letters = [
  ["A","🍎"],["B","🎈"],["C","🚗"],["D","🐬"],["E","🥚"],["F","🐟"],
  ["G","🦒"],["K","🐱"],["M","🐵"],["S","☀️"]
];

let currentGame = null;
let level = 1;
let score = 0;
let attempts = 0;
let selected = null;
let correctCount = 0;
let needed = 0;

const menu = document.getElementById("menu");
const gameArea = document.getElementById("gameArea");
const targets = document.getElementById("targets");
const choices = document.getElementById("choices");
const questionArea = document.getElementById("questionArea");
const message = document.getElementById("message");
const failMessage = document.getElementById("failMessage");

games.forEach(g => {
  const c = document.createElement("div");
  c.className = "card";
  c.innerHTML = `<div class="icon">${g.icon}</div><h3>${g.title}</h3><p>20 seviyeli oyun</p>`;
  c.onclick = () => startGame(g.id);
  menu.appendChild(c);
});

function shuffle(a){ return [...a].sort(()=>Math.random()-.5); }
function countByLevel(){ return Math.min(3 + Math.floor(level/3), 8); }

function updateBadges(){
  levelBadge.innerHTML = `Seviye ${level}/20`;
  scoreBadge.innerHTML = `Puan ${score}`;
  attemptBadge.innerHTML = `Deneme ${attempts}`;
  totalScore.innerHTML = score;
  attemptCount.innerHTML = attempts;
}

function logAttempt(game, result, points){
  const row = document.createElement("div");
  row.className = "row";
  row.innerHTML = `<span>${game} L${level} ${result}</span><b>${points}</b>`;
  scoreTable.prepend(row);
}

function resetToStart(){
  failMessage.innerHTML = "Yanlış cevap! Başa dönüyorsun 🙂";
  logAttempt(currentGame, "❌", 0);
  level = 1;
  selected = null;
  setTimeout(loadCurrentGame, 900);
}

function successLevel(){
  const points = level * 10;
  score += points;
  logAttempt(currentGame, "✅", "+" + points);
  message.innerHTML = "Success 🎉";

  if(level === 20){
    message.innerHTML = "Tebrikler! Oyunu tamamladın 🏆";
  } else {
    level++;
    setTimeout(loadCurrentGame, 800);
  }
}

function startGame(id){
  currentGame = id;
  level = 1;
  selected = null;
  menu.style.display = "none";
  gameArea.style.display = "block";
  loadCurrentGame();
}

function goHome(){
  gameArea.style.display = "none";
  menu.style.display = "grid";
}

function clearGame(){
  targets.innerHTML = "";
  choices.innerHTML = "";
  questionArea.innerHTML = "";
  message.innerHTML = "";
  failMessage.innerHTML = "";
  selected = null;
  correctCount = 0;
  updateBadges();
}

function loadCurrentGame(){
  clearGame();
  const title = games.find(g=>g.id===currentGame).title;
  gameTitle.innerHTML = title;

  if(currentGame==="shape") loadMatch(shapes, "shape");
  if(currentGame==="color") loadColor();
  if(currentGame==="number") loadNumber();
  if(currentGame==="memory") loadMemory();
  if(currentGame==="animal") loadAnimal();
  if(currentGame==="letter") loadLetters();
  if(currentGame==="pattern") loadPattern();
  if(currentGame==="compare") loadCompare();
}

/* Ortak eşleştirme */
function makeChoice(id, html){
  const c = document.createElement("div");
  c.className = "choice";
  c.dataset.id = id;
  c.innerHTML = html;
  c.onclick = () => {
    document.querySelectorAll(".choice").forEach(x=>x.classList.remove("selected"));
    c.classList.add("selected");
    selected = c;
  };
  choices.appendChild(c);
}

function makeTarget(id, html="❔"){
  const t = document.createElement("div");
  t.className = "box";
  t.dataset.id = id;
  t.innerHTML = html;
  t.onclick = () => {
    if(!selected || t.classList.contains("correct")) return;
    if(selected.dataset.id === t.dataset.id){
      t.innerHTML = selected.innerHTML;
      t.classList.add("correct");
      selected.classList.add("hidden");
      correctCount++;
      if(correctCount === needed) successLevel();
    } else {
      resetToStart();
    }
  };
  targets.appendChild(t);
}

function loadMatch(data){
  needed = countByLevel();
  const selectedData = shuffle(data).slice(0, needed);
  selectedData.forEach(x => makeTarget(x[0]));
  shuffle(selectedData).forEach(x => makeChoice(x[0], x[1]));
}

function loadColor(){
  needed = Math.min(countByLevel(), colors.length);
  const selectedData = shuffle(colors).slice(0, needed);
  selectedData.forEach(c => makeTarget(c[0], c[1]));
  shuffle(selectedData).forEach(c => {
    const ch = document.createElement("div");
    ch.className = "choice";
    ch.dataset.id = c[0];
    ch.style.background = c[2];
    ch.onclick = () => {
      document.querySelectorAll(".choice").forEach(x=>x.classList.remove("selected"));
      ch.classList.add("selected");
      selected = ch;
    };
    choices.appendChild(ch);
  });
}

function loadAnimal(){
  needed = Math.min(countByLevel(), animals.length);
  const data = shuffle(animals).slice(0, needed);
  data.forEach(a => makeTarget(a[0], a[2]));
  shuffle(data).forEach(a => makeChoice(a[0], a[1]));
}

function loadLetters(){
  needed = Math.min(countByLevel(), letters.length);
  const data = shuffle(letters).slice(0, needed);
  data.forEach(l => makeTarget(l[0], l[0]));
  shuffle(data).forEach(l => makeChoice(l[0], l[1]));
}

let currentNumber = 0;
function loadNumber(){
  currentNumber = Math.min(3 + level, 20);
  const item = level < 8 ? "🍎" : level < 15 ? "⭐" : "🐟";
  questionArea.innerHTML = `<div style="font-size:42px">${item.repeat(currentNumber)}</div>
  <input id="numInput" type="number" placeholder="Kaç tane?">
  <br><button onclick="checkNumber()">Kontrol Et</button>`;
}

function checkNumber(){
  attempts++;
  if(Number(numInput.value) === currentNumber){
    successLevel();
  } else {
    resetToStart();
  }
  updateBadges();
}

function loadMemory(){
  const pairCount = Math.min(2 + Math.floor(level/3), 8);
  const icons = shuffle(["🐶","🐱","🐰","🦊","🐵","🦁","🐼","🐸"]).slice(0,pairCount);
  const cards = shuffle([...icons,...icons]);
  let first = null, lock = false, found = 0;

  cards.forEach(icon=>{
    const card = document.createElement("div");
    card.className = "box";
    card.dataset.icon = icon;
    card.innerHTML = "❓";
    card.onclick = () => {
      if(lock || card.classList.contains("correct") || card === first) return;
      card.innerHTML = icon;
      if(!first){ first = card; }
      else {
        if(first.dataset.icon === card.dataset.icon){
          first.classList.add("correct");
          card.classList.add("correct");
          first = null;
          found++;
          if(found === pairCount) successLevel();
        } else {
          lock = true;
          setTimeout(()=>{
            attempts++;
            first.innerHTML = "❓";
            card.innerHTML = "❓";
            first = null;
            lock = false;
            resetToStart();
          },600);
        }
      }
    };
    targets.appendChild(card);
  });
}

function loadPattern(){
  const nums = Array.from({length:4 + Math.floor(level/4)},(_,i)=>i+1);
  const missing = nums[Math.floor(Math.random()*nums.length)];
  questionArea.innerHTML = `<h3>Sıradaki eksik sayıyı bul</h3>
    <div style="font-size:36px">${nums.map(n=>n===missing?"❔":n).join(" - ")}</div>`;
  needed = 1;
  shuffle(nums).forEach(n=>makeChoice(String(n), String(n)));
  makeTarget(String(missing), "Cevap");
}

function loadCompare(){
  const a = Math.floor(Math.random()*(level+5))+1;
  const b = Math.floor(Math.random()*(level+5))+1;
  const answer = a > b ? ">" : a < b ? "<" : "=";

  questionArea.innerHTML = `<h2>${a} ? ${b}</h2>`;
  needed = 1;
  [">","<","="].forEach(x=>makeChoice(x,x));
  makeTarget(answer,"Cevap");
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
