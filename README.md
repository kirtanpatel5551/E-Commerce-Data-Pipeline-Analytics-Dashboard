# E-Commerce Data Pipeline & Analytics Dashboard
Portfolio project using Python ETL, FastAPI, SQLAlchemy, React, SQL, Docker and PyTest.

## Run
Backend:
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m app.etl
python -m uvicorn app.main:app --reload
```
Frontend (new terminal):
```powershell
cd frontend
npm install
npm run dev
```
Open http://localhost:5173 and API docs at http://127.0.0.1:8000/docs.

SQLite is the zero-setup default. Set DATABASE_URL to a PostgreSQL SQLAlchemy URL for PostgreSQL.
