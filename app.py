from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret123"

events = [
    {"id": 1, "name": "Music Concert", "date": "10 April 2026", "venue": "Delhi"},
    {"id": 2, "name": "Tech Fest", "date": "15 April 2026", "venue": "Gurgaon"},
    {"id": 3, "name": "Art Exhibition", "date": "20 April 2026", "venue": "Noida"},
    {"id": 4, "name": "Food Carnival", "date": "25 April 2026", "venue": "Faridabad"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/events")
def show_events():
    return render_template("events.html", events=events)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            flash("All fields are required!", "error")
        else:
            flash("Registration Successful!", "success")

        return redirect(url_for("register"))

    return render_template("register.html", events=events)

@app.route("/admin")
def admin():
    return render_template("admin.html", events=events)

@app.route("/admin/add", methods=["POST"])
def add_event():
    name = request.form.get("name")
    date = request.form.get("date")
    venue = request.form.get("venue")

    new_event = {
        "id": len(events) + 1,
        "name": name,
        "date": date,
        "venue": venue
    }
    events.append(new_event)
    return redirect(url_for("admin"))

@app.route("/admin/delete/<int:id>")
def delete_event(id):
    global events
    events = [e for e in events if e["id"] != id]
    return redirect(url_for("admin"))

if __name__ == "__main__":
    app.run(debug=True)

    