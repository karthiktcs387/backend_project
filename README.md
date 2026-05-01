#  Backend Project – Python Full Stack (Flask)

##  Overview
This project is a **Python Full Stack Application** built using Flask and SQLite.  
It includes **Admin Authentication** and **Opportunity Management (CRUD)** with a connected frontend (HTML, CSS, JS).

---

## Tech Stack
- Backend: Python, Flask
- Database: SQLite
- Frontend: HTML, CSS, JavaScript
- Tools: Postman, Git, GitHub

---

##  Features

###  Authentication
- Admin Signup
- Admin Login
- Forgot Password (mock API)

###  Opportunity Management
- Add Opportunity
- View All Opportunities (admin-specific)
- Update Opportunity
- Delete Opportunity

###  Security
- Admin-based data isolation
- Only owner can update/delete records

---

## Project Structure


backend_project/
│
├── app.py
├── models.py
├── routes/
│ ├── auth.py
│ └── opportunity.py
│
├── Test1/
│ └── sky/
│ ├── admin.html
│ ├── admin.js
│ └── admin.css
│
├── requirements.txt
└── README.md


---

##  Setup Instructions

###  1. Clone Repository

git clone https://github.com/your-username/backend_project.git

cd backend_project


---

###  2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate # Windows


---

###  3. Install Dependencies

pip install -r requirements.txt


---

###  4. Run Backend Server

python app.py


Server runs on:

http://127.0.0.1:5000


---

###  5. Run Frontend
Open in browser:

Test1/sky/admin.html


---

##  API Endpoints

###  Auth APIs
- `POST /signup`
- `POST /login`
- `POST /forgot-password`

---

###  Opportunity APIs
- `POST /add`
- `GET /all/<admin_id>`
- `PUT /update/<id>`
- `DELETE /delete/<id>`

---

##  Testing
Use Postman or frontend UI to test APIs.

---

##  Future Improvements
- JWT Authentication
- Password hashing (bcrypt)
- Deploy on cloud (Render / AWS)
- Add user roles

---

##  Author
**Karthik**

---

## 📌 GitHub Repository
https://github.com/your-username/backend_project
