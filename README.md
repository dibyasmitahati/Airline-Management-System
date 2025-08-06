# Airlines Management System

A simple yet functional web-based Airlines Management System built with Flask. This application allows users to manage flights, bookings, user authentication, and view booking history.

---

## Deployed at
## [https://airlines-management-system.onrender.com]

---

## 🚀 Features

- User Registration & Login  
- View Available Flights  
- Book Flights  
- View Booking History  
- Admin Panel (Manage Flights & Users)  
- Secure Passwords with Hashing  

---

## 🛠 Tech Stack

- *Frontend*: HTML5, CSS3, Bootstrap  
- *Backend*: Python (Flask Framework)  
- *Database*: SQLite  
- *Other Tools*: Jinja2, Werkzeug Security  

---

## 📁 Folder Structure

Airlines-Management-System/
- │
- ├── app.py                  # Main Flask application
- ├── init_db.py              # Script to initialize DB
- ├── requirements.txt        # All Python dependencies
- ├── README.md               # Project documentation
- ├── airlinez_test.db        # SQLite database (can be ignored or gitignored)
- ├── schema.sql              # Database schema
- ├── .gitignore              # Files/folders to exclude from git
- │
- ├── static/                 # Static files: CSS, JS, Images
- │   └── ...
- │
- ├── templates/              # HTML files (Jinja templates)
- │   └── ...
- │
- └── venv/                   # Virtual environment (should be gitignored)

---

## ⚙ How to Run the Project Locally

1. Clone the Repository
2. Set Up Virtual Environment
3. Install Dependencies
4. Run the Application

---

## 📌 Notes
- Admin credentials are stored in the database file airlinez_test.db.
- To reset or reinitialize the database, use schema.sql or init_db.py.
- The app runs locally using Flask’s built-in development server.

---

## 🤝 Contributions

- This was a group project developed as part of a learning initiative.
- Feel free to fork, customize, and build upon it.
