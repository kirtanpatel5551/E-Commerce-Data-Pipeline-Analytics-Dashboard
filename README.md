# E-Commerce Data Pipeline & Analytics Dashboard

A full-stack data engineering and analytics project that processes e-commerce data through a Python ETL pipeline, stores the cleaned data in a relational database, exposes analytics through FastAPI REST APIs, and displays business insights using a React dashboard.

## 🚀 Features

- Extracts e-commerce data from CSV files
- Cleans and transforms data using Python and Pandas
- Loads processed data into a relational database
- Supports SQLite for local development
- PostgreSQL-ready database configuration
- RESTful analytics APIs built with FastAPI
- Interactive React dashboard
- Displays revenue, orders, customers, and product metrics
- Monthly sales analytics
- Top-selling product analysis
- Recent order tracking
- Automated API testing with PyTest
- Docker support for containerized deployment

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pandas
- PyTest
- Uvicorn

### Frontend
- React.js
- JavaScript
- Vite
- CSS

### Database
- SQLite
- PostgreSQL

### DevOps & Tools
- Docker
- Docker Compose
- Git
- GitHub

## 📁 Project Structure

```text
ecommerce-data-pipeline/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── etl.py
│   │   └── main.py
│   │
│   ├── data/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   └── orders.csv
│   │
│   ├── tests/
│   │   └── test_api.py
│   │
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── Dockerfile
│   ├── index.html
│   └── package.json
│
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

## ⚙️ How the Project Works

The application follows a simple data pipeline architecture:

```text
CSV Data
   ↓
Python + Pandas ETL
   ↓
SQLite / PostgreSQL
   ↓
FastAPI REST API
   ↓
React Dashboard
   ↓
Analytics & Business Insights
```

The ETL pipeline reads customer, product, and order data from CSV files, removes invalid or duplicate records, transforms the data, and loads it into the database.

FastAPI then retrieves and aggregates the stored data and provides analytics endpoints that are consumed by the React frontend.

## 📊 Dashboard Analytics

The dashboard provides several useful business metrics:

- Total Revenue
- Total Orders
- Total Customers
- Total Products
- Monthly Revenue
- Top Selling Products
- Recent Orders

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API status |
| GET | `/analytics/summary` | Get overall business metrics |
| GET | `/analytics/monthly-sales` | Get monthly revenue |
| GET | `/analytics/top-products` | Get top-selling products |
| GET | `/orders` | Get recent orders |

FastAPI automatically provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## 💻 Run the Project Locally

### 1. Backend Setup

Navigate to the backend folder:

```powershell
cd backend
```

Create a virtual environment:

```powershell
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the ETL pipeline:

```powershell
python -m app.etl
```

Start the FastAPI server:

```powershell
python -m uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### 2. Frontend Setup

Open a **second terminal** and navigate to the frontend folder:

```powershell
cd frontend
```

Install the dependencies:

```powershell
npm install
```

Start the React application:

```powershell
npm run dev
```

Open the application at:

```text
http://localhost:5173
```

## 🧪 Testing

From the backend directory, run:

```powershell
python -m pytest
```

## 🐳 Docker

The project also contains Docker configuration for running the frontend, backend, and PostgreSQL database as containers.

```powershell
docker compose up --build
```

## 🎯 Project Purpose

This project was developed to demonstrate practical experience with:

- Python backend development
- ETL pipeline development
- Data cleaning and transformation
- REST API development
- SQL and relational databases
- Frontend-backend integration
- Data analytics
- Automated testing
- Docker containerization
- Full-stack application architecture

## 👨‍💻 Author

**Kirtan Patel**

MS in Computer Science  
West Chester University of Pennsylvania

GitHub: `kirtanpatel5551`
