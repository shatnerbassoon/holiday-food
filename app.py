html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
body { font-family: -apple-system; padding: 15px; background: #f2f2f7; }

.section {
  background: white;
  padding: 12px;
  border-radius: 12px;
  margin-bottom: 15px;
  max-height: 400px;
  overflow-y: auto;
}

details {
  margin-bottom: 10px;
  background: #fff;
  padding: 10px;
  border-radius: 10px;
}

input, textarea {
  width: 100%;
  margin-top: 5px;
  padding: 6px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

.food-item {
  border-top: 1px solid #eee;
  margin-top: 10px;
  padding-top: 10px;
}

button {
  margin-top: 8px;
  padding: 6px 10px;
  border-radius: 8px;
}
</style>
</head>

<body>

<h1>🥗 Holiday Food Tracker</h1>

<div class="section">
<h2>📅 Daily Diary</h2>

Start Date: <input type="date" id="startDate">
End Date: <input type="date" id="endDate">

<button onclick="generateDays()">Generate Days</button>

<div id="daysContainer"></div>
</div>

<div class="section">
<h2>🍽 Restaurants</h2>

<button onclick="addRestaurant()">Add Restaurant</button>
<div id="restaurantContainer"></div>
</div>

<script>

// ===== SAVE / LOAD =====
function save(key, data) {
  localStorage.setItem(key, JSON.stringify(data));
}

function load(key, fallback) {
  return JSON.parse(localStorage.getItem(key)) || fallback;
}

// ===== DAYS =====
function generateDays() {
  const start = new Date(document.getElementById("startDate").value);
  const end = new Date(document.getElementById("endDate").value);

  let days = [];

  for (let d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) {
    days.push({
      date: new Date(d),
      foods: []
    });
  }

  save("days", days);
  renderDays();
}

function renderDays() {
  const container = document.getElementById("daysContainer");
  container.innerHTML = "";

  const days = load("days", []);

  days.forEach((day, i) => {
    const label = new Date(day.date).toDateString();

    let html = `
      <details>
        <summary>${label}</summary>
        <button onclick="addFood(${i})">Add Food</button>
    `;

    day.foods.forEach((food, j) => {
      html += renderFood(i, j, food);
    });

    html += "</details>";
    container.innerHTML += html;
  });
}

// ===== FOOD =====
function renderFood(dayIndex, foodIndex, food) {
  return `
  <div class="food-item">
    <input placeholder="Name" value="${food.name || ''}" onchange="updateFood(${dayIndex},${foodIndex},'name',this.value)">
    <input placeholder="Calories" value="${food.calories || ''}" onchange="updateFood(${dayIndex},${foodIndex},'calories',this.value)">
    <input placeholder="Fat" value="${food.fat || ''}" onchange="updateFood(${dayIndex},${foodIndex},'fat',this.value)">
    <input placeholder="Sat Fat" value="${food.satfat || ''}" onchange="updateFood(${dayIndex},${foodIndex},'satfat',this.value)">
    <input placeholder="Fibre" value="${food.fibre || ''}" onchange="updateFood(${dayIndex},${foodIndex},'fibre',this.value)">
    <input placeholder="Protein" value="${food.protein || ''}" onchange="updateFood(${dayIndex},${foodIndex},'protein',this.value)">
    <input placeholder="Carbs" value="${food.carbs || ''}" onchange="updateFood(${dayIndex},${foodIndex},'carbs',this.value)">
    <input placeholder="Sugar" value="${food.sugar || ''}" onchange="updateFood(${dayIndex},${foodIndex},'sugar',this.value)">
    <textarea placeholder="Notes" onchange="updateFood(${dayIndex},${foodIndex},'notes',this.value)">${food.notes || ''}</textarea>
  </div>
  `;
}

function addFood(dayIndex) {
  const days = load("days", []);
  days[dayIndex].foods.push({});
  save("days", days);
  renderDays();
}

function updateFood(dayIndex, foodIndex, field, value) {
  const days = load("days", []);
  days[dayIndex].foods[foodIndex][field] = value;
  save("days", days);
}

// ===== RESTAURANTS =====
function addRestaurant() {
  const data = load("restaurants", []);
  data.push({ name: "", meals: [] });
  save("restaurants", data);
  renderRestaurants();
}

function renderRestaurants() {
  const container = document.getElementById("restaurantContainer");
  container.innerHTML = "";

  const data = load("restaurants", []);

  data.forEach((r, i) => {
    let html = `
    <details>
      <summary>
        <input value="${r.name}" placeholder="Restaurant name" onchange="updateRestaurant(${i}, this.value)">
      </summary>
      <button onclick="addMeal(${i})">Add Meal</button>
    `;

    r.meals.forEach((m, j) => {
      html += `
        <input value="${m}" placeholder="Meal name" onchange="updateMeal(${i},${j},this.value)">
      `;
    });

    html += "</details>";
    container.innerHTML += html;
  });
}

function updateRestaurant(i, value) {
  const data = load("restaurants", []);
  data[i].name = value;
  save("restaurants", data);
}

function addMeal(i) {
  const data = load("restaurants", []);
  data[i].meals.push("");
  save("restaurants", data);
  renderRestaurants();
}

function updateMeal(i, j, value) {
  const data = load("restaurants", []);
  data[i].meals[j] = value;
  save("restaurants", data);
}

// ===== INIT =====
renderDays();
renderRestaurants();

</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generated!")