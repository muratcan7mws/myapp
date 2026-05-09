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
* { box-sizing: border-box; }

body {
  margin:0;
  font-family:Arial,sans-serif;
  color:#1e293b;
  min-height:100vh;
  overflow-x:hidden;
  background:
    radial-gradient(circle at 8% 15%, #fde68a 0 42px, transparent 43px),
    radial-gradient(circle at 90% 12%, #f9a8d4 0 54px, transparent 55px),
    radial-gradient(circle at 18% 85%, #93c5fd 0 60px, transparent 61px),
    radial-gradient(circle at 88% 78%, #86efac 0 50px, transparent 51px),
    linear-gradient(135deg,#fef3c7,#e0f2fe,#fce7f3);
  background-attachment:fixed;
}

body::before {
  content:"🌈 ⭐ 🎈 🧸 🚀 🍭 ☁️";
  position:fixed;
  top:20px;
  left:0;
  width:100%;
  text-align:center;
  font-size:42px;
  opacity:.22;
  pointer-events:none;
}

.container {
  max-width:1300px;
  margin:auto;
  padding:24px;
  position:relative;
  z-index:1;
}

h1,h2 {
  color:#312e81;
  text-align:center;
}

.subtitle {
  text-align:center;
  font-size:18px;
  color:#475569;
  font-weight:bold;
}

.layout {
  display:grid;
  grid-template-columns:1fr 310px;
  gap:20px;
}

.menu {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:18px;
}

.card,.panel,.game {
  background:rgba(255,255,255,0.94);
  border-radius:28px;
  padding:22px;
  box-shadow:0 14px 40px rgba(15,23,42,.14);
  border:3px solid rgba(255,255,255,.9);
}

.card {
  cursor:pointer;
  text-align:center;
  transition:.2s;
}

.card:hover {
  transform:translateY(-5px) scale(1.02);
}

.icon {
  font-size:56px;
}

.game {
  display:none;
  text-align:center;
}

.items {
  display:flex;
  flex-wrap:wrap;
  justify-content:center;
  gap:14px;
  margin-top:20px;
}

.box,.choice {
  width:102px;
  height:92px;
  border-radius:22px;
  border:2px solid #cbd5e1;
  background:#f8fafc;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:30px;
  cursor:grab;
  user-select:none;
  text-align:center;
  padding:7px;
  line-height:1.05;
  overflow:hidden;
  white-space:normal;
  word-break:normal;
  overflow-wrap:normal;
  transition:.18s;
  touch-action:none;
}

.box {
  font-size:17px;
  font-weight:bold;
}

.choice.dragging {
  opacity:.8;
  transform:scale(1.12);
  position:fixed;
  z-index:9999;
  pointer-events:none;
}

.choice.selected {
  border-color:#4f46e5;
  background:#eef2ff;
  transform:scale(1.07);
}

.correct {
  background:#dcfce7 !important;
  border-color:#22c55e !important;
  animation: correctGlow .55s ease-in-out;
}

@keyframes correctGlow {
  0% { transform:scale(1); box-shadow:0 0 0 rgba(34,197,94,0); }
  50% { transform:scale(1.12); box-shadow:0 0 28px rgba(34,197,94,.8); }
  100% { transform:scale(1); box-shadow:0 0 0 rgba(34,197,94,0); }
}

.hidden { visibility:hidden; }

button {
  border:none;
  border-radius:16px;
  padding:13px 22px;
  background:#4f46e5;
  color:white;
  font-weight:bold;
  cursor:pointer;
  margin:8px;
  font-size:15px;
}

.back { background:#64748b; }

.success {
  color:#16a34a;
  font-size:24px;
  font-weight:bold;
  min-height:34px;
}

.fail {
  color:#dc2626;
  font-size:22px;
  font-weight:bold;
  min-height:34px;
}

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
  max-height:560px;
  overflow:auto;
  margin-top:10px;
}

.row {
  display:block;
  border-bottom:1px solid #e2e8f0;
  padding:10px 0;
}

.row span {
  display:block;
  color:#334155;
  line-height:1.35;
}

.row b {
  display:block;
  margin-top:4px;
  color:#312e81;
}

input {
  padding:14px;
  border-radius:12px;
  border:1px solid #cbd5e1;
  font-size:20px;
  text-align:center;
}

.confetti {
  position:fixed;
  top:-20px;
  font-size:24px;
  z-index:99999;
  animation: fall 2.2s linear forwards;
  pointer-events:none;
}

@keyframes fall {
  to {
    transform:translateY(110vh) rotate(720deg);
    opacity:0;
  }
}

.story-card {
  max-width: 820px;
  margin: 20px auto;
  background: #fff7ed;
  border: 3px solid #fed7aa;
  border-radius: 30px;
  padding: 24px;
  box-shadow: 0 14px 35px rgba(15,23,42,.12);
}

.story-scene {
  font-size: 88px;
  margin: 14px 0;
  line-height: 1.2;
}

.story-text {
  font-size: 20px;
  line-height: 1.65;
  font-weight: bold;
  color: #334155;
}

.story-options {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 18px;
}

.story-option {
  min-width: 150px;
  min-height: 90px;
  border-radius: 22px;
  background: #eef2ff;
  border: 2px solid #818cf8;
  color: #312e81;
  font-size: 22px;
  font-weight: bold;
  cursor: pointer;
  padding: 14px;
}

.story-controls button {
  background: #f97316;
}

@media(max-width:900px){
  .layout { grid-template-columns:1fr; }

  .box,.choice {
    width:86px;
    height:78px;
    font-size:24px;
    padding:5px;
  }

  .box { font-size:14px; }

  h1 { font-size:30px; }

  .story-scene { font-size:60px; }

  .story-text { font-size:17px; }

  .story-option {
    min-width: 130px;
    font-size: 18px;
  }
}
</style>
</head>

<body>
<div class="container">
<h1>Çocuk Oyunları 🎈</h1>
<p class="subtitle">9 farklı oyun, 20 seviye, puan sistemi ve eğlenceli öğrenme!</p>

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
    <div>Toplam Deneme: <b id="attemptCount">0</b></div>
    <hr>
    <div id="scoreTable" class="score-table"></div>
  </aside>
</div>
</div>

<script>
const games = [
  {id:"shape", title:"Şekil Eşleştirme", icon:"🔺", desc:"Şekilleri doğru kutulara yerleştir."},
  {id:"color", title:"Renk Eşleştirme", icon:"🎨", desc:"Renkleri doğru isimlerle eşleştir."},
  {id:"number", title:"Sayı Oyunu", icon:"🔢", desc:"Nesneleri say ve doğru cevabı yaz."},
  {id:"memory", title:"Hafıza Oyunu", icon:"🧠", desc:"Aynı kartları bul."},
  {id:"animal", title:"Hayvan Eşleştirme", icon:"🐶", desc:"Hayvanları isimleriyle eşleştir."},
  {id:"letter", title:"Harf Oyunu", icon:"🔤", desc:"Harfleri ilgili nesnelerle eşleştir."},
  {id:"pattern", title:"Sıralama Oyunu", icon:"🧩", desc:"Eksik sayıyı bul."},
  {id:"compare", title:"Büyük-Küçük Oyunu", icon:"⚖️", desc:"Büyük, küçük veya eşit olanı bul."},
  {id:"story", title:"Hikaye Oyunu", icon:"📖", desc:"Seçim yap, hikaye değişsin."}
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
let dragClone = null;
let draggedChoice = null;

let storyState = {
  character: null,
  fruit: null,
  animal: null,
  currentText: ""
};

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
  c.innerHTML = `
    <div class="icon">${g.icon}</div>
    <h3>${g.title}</h3>
    <p>${g.desc}</p>
    <b>${g.id === "story" ? "Sesli İnteraktif Hikaye" : "20 Seviye"}</b>
  `;
  c.onclick = () => startGame(g.id);
  menu.appendChild(c);
});

function shuffle(a){ return [...a].sort(()=>Math.random()-.5); }
function countByLevel(){ return Math.min(3 + Math.floor(level/3), 8); }

function getGameTitle(id){
  const game = games.find(g => g.id === id);
  return game ? game.title : id;
}

function updateBadges(){
  levelBadge.innerHTML = currentGame === "story" ? "Hikaye Modu" : `Seviye ${level}/20`;
  scoreBadge.innerHTML = `Puan ${score}`;
  attemptBadge.innerHTML = `Deneme ${attempts}`;
  totalScore.innerHTML = score;
  attemptCount.innerHTML = attempts;
}

function logAttempt(game, result, points){
  attempts++;
  const row = document.createElement("div");
  row.className = "row";

  const statusText = result === "✅"
    ? "Başarılı tamamlandı"
    : "Yanlış cevap verildi, oyun başa döndü";

  const pointText = result === "✅"
    ? `+${points} puan kazandın`
    : "0 puan";

  row.innerHTML = `
    <span>${getGameTitle(game)} - ${game === "story" ? "Hikaye tamamlandı" : "Seviye " + level}</span>
    <span>${statusText}</span>
    <b>${pointText}</b>
  `;

  scoreTable.prepend(row);
  updateBadges();
}

function confetti(){
  const emojis = ["🎉","⭐","🎈","🌈","🍭","✨","🧸"];
  for(let i=0;i<45;i++){
    const el = document.createElement("div");
    el.className = "confetti";
    el.innerHTML = emojis[Math.floor(Math.random()*emojis.length)];
    el.style.left = Math.random()*100 + "vw";
    el.style.animationDuration = (1.6 + Math.random()*1.4) + "s";
    document.body.appendChild(el);
    setTimeout(()=>el.remove(),3000);
  }
}

function resetToStart(){
  failMessage.innerHTML = "Yanlış cevap! Oyun başa dönüyor 🙂";
  logAttempt(currentGame, "❌", 0);
  level = 1;
  selected = null;
  correctCount = 0;
  setTimeout(loadCurrentGame, 900);
}

function successLevel(){
  const points = level * 10;
  score += points;
  logAttempt(currentGame, "✅", points);
  message.innerHTML = "Harika! Doğru cevap 🎉";

  if(level === 20){
    message.innerHTML = "Tebrikler! Bu oyunun tüm seviyelerini tamamladın 🏆";
    confetti();
  } else {
    level++;
    setTimeout(loadCurrentGame, 850);
  }
}

function startGame(id){
  currentGame = id;
  level = 1;
  selected = null;
  correctCount = 0;
  stopStoryVoice();
  menu.style.display = "none";
  gameArea.style.display = "block";
  loadCurrentGame();
}

function goHome(){
  stopStoryVoice();
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

  if(currentGame==="shape") loadMatch(shapes);
  if(currentGame==="color") loadColor();
  if(currentGame==="number") loadNumber();
  if(currentGame==="memory") loadMemory();
  if(currentGame==="animal") loadAnimal();
  if(currentGame==="letter") loadLetters();
  if(currentGame==="pattern") loadPattern();
  if(currentGame==="compare") loadCompare();
  if(currentGame==="story") loadStory();
}

function selectChoice(c){
  document.querySelectorAll(".choice").forEach(x=>x.classList.remove("selected"));
  c.classList.add("selected");
  selected = c;
}

function enableDrag(choice){
  choice.addEventListener("pointerdown", e => {
    if(choice.classList.contains("hidden")) return;

    draggedChoice = choice;
    selected = choice;

    dragClone = choice.cloneNode(true);
    dragClone.classList.add("dragging");
    dragClone.style.left = e.clientX - 45 + "px";
    dragClone.style.top = e.clientY - 45 + "px";
    document.body.appendChild(dragClone);

    choice.setPointerCapture(e.pointerId);
  });

  choice.addEventListener("pointermove", e => {
    if(!dragClone) return;
    dragClone.style.left = e.clientX - 45 + "px";
    dragClone.style.top = e.clientY - 45 + "px";
  });

  choice.addEventListener("pointerup", e => {
    if(!dragClone) return;

    dragClone.remove();
    dragClone = null;

    const elem = document.elementFromPoint(e.clientX, e.clientY);
    const target = elem ? elem.closest(".box") : null;

    if(target){
      handleTarget(target);
    }

    draggedChoice = null;
  });
}

function makeChoice(id, html){
  const c = document.createElement("div");
  c.className = "choice";
  c.dataset.id = id;
  c.innerHTML = html;
  c.onclick = () => selectChoice(c);
  enableDrag(c);
  choices.appendChild(c);
}

function makeTarget(id, html="❔"){
  const t = document.createElement("div");
  t.className = "box";
  t.dataset.id = id;
  t.innerHTML = html;
  t.onclick = () => handleTarget(t);
  targets.appendChild(t);
}

function handleTarget(t){
  if(!selected || t.classList.contains("correct")) return;

  if(selected.dataset.id === t.dataset.id){
    t.innerHTML = selected.innerHTML;
    t.classList.add("correct");
    selected.classList.add("hidden");
    correctCount++;

    if(correctCount === needed){
      successLevel();
    }
  } else {
    resetToStart();
  }
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
    ch.onclick = () => selectChoice(ch);
    enableDrag(ch);
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

  questionArea.innerHTML = `
    <div style="font-size:42px;line-height:1.4;margin:18px;">${item.repeat(currentNumber)}</div>
    <input id="numInput" type="number" placeholder="Kaç tane?">
    <br>
    <button onclick="checkNumber()">Kontrol Et</button>
  `;
}

function checkNumber(){
  if(Number(numInput.value) === currentNumber){
    successLevel();
  } else {
    resetToStart();
  }
}

function loadMemory(){
  const pairCount = Math.min(2 + Math.floor(level/3), 8);
  const icons = shuffle(["🐶","🐱","🐰","🦊","🐵","🦁","🐼","🐸"]).slice(0,pairCount);
  const cards = shuffle([...icons,...icons]);
  let first = null;
  let lock = false;
  let found = 0;

  cards.forEach(icon=>{
    const card = document.createElement("div");
    card.className = "box";
    card.dataset.icon = icon;
    card.innerHTML = "❓";

    card.onclick = () => {
      if(lock || card.classList.contains("correct") || card === first) return;

      card.innerHTML = icon;

      if(!first){
        first = card;
      } else {
        if(first.dataset.icon === card.dataset.icon){
          first.classList.add("correct");
          card.classList.add("correct");
          first = null;
          found++;

          if(found === pairCount){
            successLevel();
          }
        } else {
          lock = true;
          setTimeout(()=>{
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

  questionArea.innerHTML = `
    <h3>Eksik sayıyı bul</h3>
    <div style="font-size:36px;margin:18px;">${nums.map(n=>n===missing?"❔":n).join(" - ")}</div>
  `;

  needed = 1;
  shuffle(nums).forEach(n=>makeChoice(String(n), String(n)));
  makeTarget(String(missing),"Cevap");
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

/* HIKAYE OYUNU */

function speakStory(text) {
  if (!("speechSynthesis" in window)) {
    alert("Bu tarayıcı seslendirmeyi desteklemiyor.");
    return;
  }

  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "tr-TR";
  utterance.rate = 0.88;
  utterance.pitch = storyState.character === "girl" ? 1.45 : 1.15;

  const voices = window.speechSynthesis.getVoices();
  const trVoice = voices.find(v => v.lang && v.lang.toLowerCase().includes("tr"));
  if (trVoice) utterance.voice = trVoice;

  window.speechSynthesis.speak(utterance);
}

function stopStoryVoice() {
  if ("speechSynthesis" in window) window.speechSynthesis.cancel();
}

function pauseStoryVoice() {
  if ("speechSynthesis" in window) window.speechSynthesis.pause();
}

function resumeStoryVoice() {
  if ("speechSynthesis" in window) window.speechSynthesis.resume();
}

function storyBox(scene, text, optionsHtml = "") {
  storyState.currentText = text;

  questionArea.innerHTML = `
    <div class="story-card">
      <div class="story-scene">${scene}</div>
      <div class="story-text">${text}</div>

      <div class="story-controls">
        <button onclick="speakStory(storyState.currentText)">Seslendir 🔊</button>
        <button onclick="pauseStoryVoice()">Durdur ⏸️</button>
        <button onclick="resumeStoryVoice()">Devam Et ▶️</button>
        <button onclick="stopStoryVoice()">Sesi Kapat 🔇</button>
      </div>

      <div class="story-options">
        ${optionsHtml}
      </div>
    </div>
  `;

  setTimeout(() => speakStory(text), 300);
}

function loadStory() {
  targets.innerHTML = "";
  choices.innerHTML = "";
  message.innerHTML = "";
  failMessage.innerHTML = "";

  storyState = {
    character: null,
    fruit: null,
    animal: null,
    currentText: ""
  };

  updateBadges();

  storyBox(
    "👧 👦",
    "Hikayeye başlamadan önce kahramanını seç. Kız çocuk mu, erkek çocuk mu?",
    `
      <button class="story-option" onclick="selectStoryCharacter('girl')">👧 Kız Çocuk</button>
      <button class="story-option" onclick="selectStoryCharacter('boy')">👦 Erkek Çocuk</button>
    `
  );
}

function selectStoryCharacter(character) {
  storyState.character = character;

  const hero = character === "girl" ? "küçük kız" : "küçük çocuk";

  storyBox(
    "🏡🌲🧺",
    `Bir varmış bir yokmuş. Ormanın kenarında yaşayan sevimli bir ${hero} varmış.
     Bir gün annesi ona kırmızı bir pelerin vermiş ve büyükannesine götürmesi için küçük bir sepet hazırlamış.
     ${hero}, sepetini almış ve kuşların şarkı söylediği ormana doğru yürümeye başlamış.`,
    `<button class="story-option" onclick="storyFruitScene()">Ormana Git 🌲</button>`
  );
}

function storyFruitScene() {
  const hero = storyState.character === "girl" ? "küçük kız" : "küçük çocuk";

  storyBox(
    "🌲🍎🍐",
    `${hero}, ormanda yürürken renkli çiçekler, kelebekler ve meyve ağaçları görmüş.
     Sepetine büyükannesi için bir meyve koymak istemiş.
     Sence hangi meyveyi toplasın?`,
    `
      <button class="story-option" onclick="selectFruit('apple')">🍎 Elma</button>
      <button class="story-option" onclick="selectFruit('pear')">🍐 Armut</button>
    `
  );
}

function selectFruit(fruit) {
  storyState.fruit = fruit;

  const hero = storyState.character === "girl" ? "küçük kız" : "küçük çocuk";
  const fruitText = fruit === "apple" ? "kırmızı bir elma" : "tatlı bir armut";

  storyBox(
    fruit === "apple" ? "🍎🧺🌲" : "🍐🧺🌲",
    `${hero}, sepete ${fruitText} koymuş.
     Tam yoluna devam edecekken çalıların arasından bir ses duymuş.
     Karşısına bir hayvan çıkmış. Sence bu hayvan hangisi olsun?`,
    `
      <button class="story-option" onclick="selectAnimalStory('wolf')">🐺 Kurt</button>
      <button class="story-option" onclick="selectAnimalStory('fox')">🦊 Tilki</button>
    `
  );
}

function selectAnimalStory(animal) {
  storyState.animal = animal;

  const hero = storyState.character === "girl" ? "küçük kız" : "küçük çocuk";
  const fruitText = storyState.fruit === "apple" ? "elmayı" : "armudu";

  if (animal === "wolf") {
    storyBox(
      "🐺🌲🏠",
      `Karşısına meraklı bir kurt çıkmış. Kurt ona nereye gittiğini sormuş.
       ${hero}, büyükannesine gittiğini söylemiş ama annesinin sözünü hatırlayıp yoldan ayrılmamış.
       Sepetindeki ${fruitText} sıkıca tutmuş ve güvenli patikadan yürümeye devam etmiş.
       Sonunda büyükannesinin evine ulaşmış ve birlikte çok mutlu olmuşlar. Tebrikler, hikayeyi tamamladın!`,
      `<button class="story-option" onclick="finishStoryGame()">Hikayeyi Bitir 🏆</button>`
    );
  } else {
    storyBox(
      "🦊🌸🏠",
      `Karşısına akıllı bir tilki çıkmış. Tilki ona ormandaki en güzel çiçekleri göstermiş.
       Ama ${hero}, önce büyükannesine gitmesi gerektiğini söylemiş.
       Tilki ona güvenli yolu tarif etmiş. ${hero}, sepetindeki ${fruitText} ile büyükannesinin evine varmış.
       Büyükannesi çok sevinmiş ve birlikte güzel bir gün geçirmişler. Tebrikler, hikayeyi tamamladın!`,
      `<button class="story-option" onclick="finishStoryGame()">Hikayeyi Bitir 🏆</button>`
    );
  }
}

function finishStoryGame() {
  stopStoryVoice();
  message.innerHTML = "Hikaye tamamlandı 🎉";
  score += 100;
  logAttempt("story", "✅", 100);
  confetti();
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
