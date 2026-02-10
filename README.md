# 🎓 Campus Feedback System

A Flask-based web application that allows students to submit feedback about campus facilities and enables admins to view and filter feedback easily.

---

## 🚀 Features

- Student feedback form with:
  - Roll Number
  - Department
  - Year of Study
  - Feedback Category (Teaching, Lab, Infrastructure, Library)
  - Satisfaction level (slider)
  - Suggestions
- Admin dashboard to:
  - View all feedback records
  - Filter feedback year-wise
- Clean and responsive UI
- SQLite database for storage

---

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

campus-feedback-system/
│
├── app.py
├── database.py
├── feedback.db
├── templates/
│   ├── form.html
│   └── admin.html
├── static/
│   ├── teaching.jpg
│   ├── lab.jpg
│   ├── infra.jpg
│   └── library.jpg
└── README.md

---

## ▶️ How to Run the Project

1. Clone the repository

git clone https://github.com/Hemasri21/campus-feedback-system.git

2. Go to the project folder

cd campus-feedback-system

3. Install Flask

pip install flask

4. Run the application

python app.py

5. Open in browser

Student Form:
http://127.0.0.1:5000/

Admin Dashboard:
http://127.0.0.1:5000/admin

---

## 📌 Notes

- This project is built as a beginner-friendly full-stack application.
- Admin authentication is not implemented in this version.
- Suitable for fresher-level portfolio and learning Flask fundamentals.
