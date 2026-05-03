# TaskForge 🚀

TaskForge is a Full-Stack Team Task Management Web Application where users can create projects, assign tasks, and track progress with Role-Based Access Control (RBAC).

---

## 🌐 Live Demo

Frontend: YOUR_FRONTEND_URL  
Backend API: YOUR_BACKEND_URL/docs

---

## 📌 Features

### 🔐 Authentication
- User Signup
- User Login
- JWT Token Authentication

### 👥 Role-Based Access Control
- Admin
  - Create Tasks
  - Manage Team
  - View Dashboard
- Member
  - View Assigned Tasks
  - Track Progress

### 📋 Task Management
- Create Tasks
- Assign Tasks
- Update Task Status
- Track Pending & Completed Tasks

### 📊 Dashboard
- Total Tasks
- Completed Tasks
- Pending Tasks
- Task Cards

---

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- Tailwind CSS
- Axios
- React Router DOM

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic

### Deployment
- Frontend: Vercel
- Backend: Railway

---

## 📂 Project Structure

```bash
TaskForge/
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── railway.json
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
⚙️ Installation
1️⃣ Clone Repository
git clone YOUR_GITHUB_REPO_LINK
2️⃣ Backend Setup
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload

Backend runs on:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs
3️⃣ Frontend Setup
cd frontend

npm install

npm run dev

Frontend runs on:

http://localhost:5173
🔑 Test Credentials
Admin
Email: admin@gmail.com
Password: 123456
Member
Email: member@gmail.com
Password: 123456
