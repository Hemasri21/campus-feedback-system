from flask import Flask, render_template, request
import sqlite3
from database import create_table, insert_feedback

app = Flask(__name__)

# =========================
# CREATE TABLE ON START
# =========================
create_table()


# =========================
# STUDENT FEEDBACK FORM
# =========================
@app.route("/")
def index():
    return render_template("form.html")


# =========================
# FORM SUBMISSION
# =========================
@app.route("/submit", methods=["POST"])
def submit():
    roll = request.form.get("roll_number")
    department = request.form.get("department")
    year = request.form.get("year")
    category = request.form.get("category")
    satisfaction = request.form.get("satisfaction")
    suggestion = request.form.get("suggestion")

    insert_feedback(
        roll,
        department,
        year,
        category,
        satisfaction,
        suggestion
    )

    return "<h2>Feedback submitted successfully!</h2><a href='/'>Go Back</a>"


# =========================
# ADMIN DASHBOARD
# =========================
@app.route("/admin")
def admin():
    year = request.args.get("year")

    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()

    if year and year != "":
        cursor.execute(
            "SELECT * FROM feedback WHERE year = ?",
            (year,)
        )
    else:
        cursor.execute("SELECT * FROM feedback")

    data = cursor.fetchall()
    conn.close()

    return render_template("admin.html", feedback=data)


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)
