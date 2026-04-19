data = {
    "Land": [
        {
            "name": "Italian Bistro",
            "meals": [
                {
                    "name": "Grilled Sea Bass",
                    "stats": {
                        "Calories": 450,
                        "Fat": "18g",
                        "Sat Fat": "3g",
                        "Protein": "40g",
                        "Fibre": "4g",
                        "Carbs": "20g",
                        "Sugar": "3g"
                    }
                }
            ]
        }
    ],
    "Cruise": [
        {
            "name": "Main Dining Room",
            "meals": [
                {
                    "name": "Grilled Salmon",
                    "stats": {
                        "Calories": 500,
                        "Fat": "22g",
                        "Sat Fat": "4g",
                        "Protein": "42g",
                        "Fibre": "3g",
                        "Carbs": "18g",
                        "Sugar": "2g"
                    }
                }
            ]
        }
    ]
}

html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    font-family: -apple-system;
    padding: 15px;
    background: #f2f2f7;
}
h1 {
    margin-bottom: 10px;
}
h2 {
    margin-top: 25px;
}
details {
    margin-bottom: 10px;
    background: white;
    padding: 12px;
    border-radius: 12px;
}
summary {
    font-size: 17px;
    font-weight: 600;
}
.meal {
    margin-left: 10px;
}
.stats {
    font-size: 14px;
    margin-top: 5px;
}
textarea {
    width: 100%;
    height: 120px;
    margin-top: 10px;
    font-size: 15px;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #ccc;
}
.section {
    background: white;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 15px;
}
</style>
</head>
<body>

<h1>🥗 Healthy Eating Plan</h1>

<div class="section">
<h2>📝 Food Diary</h2>

<h3>Land Notes</h3>
<textarea id="landDiary" placeholder="What did I actually eat on land..."></textarea>

<h3>Cruise Notes</h3>
<textarea id="cruiseDiary" placeholder="What did I eat on the cruise..."></textarea>
</div>
"""

for category, restaurants in data.items():
    html += f"<h2>{category}</h2>"

    for r in restaurants:
        html += f"""
        <details>
            <summary>{r['name']}</summary>
        """

        for meal in r["meals"]:
            html += f"""
            <details class="meal">
                <summary>{meal['name']}</summary>
                <div class="stats">
            """

            for k, v in meal["stats"].items():
                if k == "Sat Fat":
                    value = int(v.replace("g", ""))
                    color = "green" if value <= 5 else "red"
                    html += f"<span style='color:{color}'>{k}: {v}</span><br>"
                else:
                    html += f"{k}: {v}<br>"

            html += """
                </div>
            </details>
            """

        html += "</details>"

html += """
<script>
function setupDiary(id, key) {
  const el = document.getElementById(id);
  el.value = localStorage.getItem(key) || "";
  el.addEventListener("input", () => {
    localStorage.setItem(key, el.value);
  });
}

setupDiary("landDiary", "landNotes");
setupDiary("cruiseDiary", "cruiseNotes");
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generated!")