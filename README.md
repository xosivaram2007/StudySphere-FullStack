# StudySphere – Fullstack Study & Task Manager

StudySphere is a **fullstack web application** that helps students organize their learning projects, tasks, and notes. It is designed as a **developed project** showcasing both backend and frontend skills.

---

## Tech Stack

- **Backend**
  - Python, **Flask**
  - **SQLAlchemy** / Flask‑SQLAlchemy (SQLite by default)
  - JWT authentication (login/register)
  - Password hashing with **passlib (bcrypt)**
  - CORS configured for a separate frontend

- **Frontend**
  - **Next.js** (App Router) + React
  - JavaScript
  - **Tailwind CSS** for styling

> Note: The backend currently lives in this repository under `backend/`. The Next.js frontend was created separately in `C:\Users\Asus\studysphere` on this machine, but can be moved into `frontend/` later to make this a single monorepo.

---

## Features (current)

- **User authentication**
  - `POST /api/auth/register` – create a new account
  - `POST /api/auth/login` – obtain a JWT access token
  - Passwords are stored as secure bcrypt hashes

- **Data model (database)**
  - `User` – basic user profile
  - `Project` – study projects belonging to a user
  - `Task` – tasks under each project (status, priority, due date)
  - `Note` – rich text notes for projects

- **Health check**
  - `GET /api/health` – simple status endpoint to verify the API is running

The Next.js frontend already includes:

- A **modern Tailwind UI**
- `/register` and `/login` pages
- Fetch helpers that call the Flask `register` and `login` endpoints

---

## Backend – Getting Started

### 1. Environment

```bash
cd "e:\porkect slay 2\backend"
python -m pip install -r requirements.txt
```

### 2. Run the API

```bash
cd "e:\porkect slay 2\backend"
python app.py
```

The API will be available at:

- `http://localhost:5000/api/health`

By default it uses a local SQLite database file `studysphere.db` in the `backend` directory.

---

## Frontend – Getting Started (current location)

Frontend was created with `create-next-app` and is currently located at:

```text
C:\Users\Asus\studysphere
```

From that folder:

```bash
cd "C:\Users\Asus\studysphere"
npm install
npm run dev
```

Then open `http://localhost:3000` in a browser.

---


