from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import os
from database import create_table, insert_feedback

app = Flask(__name__)
app.secret_key = os.urandom(24)

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
# LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect("feedback.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("admin"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# =========================
# ADMIN DASHBOARD (LOGIN + SEARCH + FILTER)
# =========================
@app.route("/admin")
def admin():

    # 🔒 LOGIN PROTECTION
    if "user" not in session:
        return redirect(url_for("login"))

    year = request.args.get("year")
    search = request.args.get("q", "")

    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()

    if search:
        cursor.execute("""
            SELECT * FROM feedback
            WHERE roll_number LIKE ? OR category LIKE ? OR suggestion LIKE ?
        """, (f"%{search}%", f"%{search}%", f"%{search}%"))

    elif year and year != "":
        cursor.execute(
            "SELECT * FROM feedback WHERE year = ?",
            (year,)
        )
    else:
        cursor.execute("SELECT * FROM feedback")

    data = cursor.fetchall()
    conn.close()

    return render_template("admin.html", feedback=data, search=search)


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)