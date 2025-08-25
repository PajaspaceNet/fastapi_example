# fastapi_example

project example fastapi  REST API v Pythonu + FastAPI
Jednoduché REST API pro správu úkolů v Pythonu + FastAPI + SQLite.

```
my-fastapi-app/
│── main.py          # Hlavní aplikace
│── models.py        # Databázové modely
│── database.py      # Připojení k DB
│── requirements.txt # Knihovny
│── README.md        # Návod k projektu
```

# Simple Task API

Jednoduché REST API pro správu úkolů v Pythonu + FastAPI + SQLite.
Tento projekt je **plně funkční, lokálně spustitelný**, ukazuje asynchronní operace, CRUD, databázi a FastAPI.  

## Spuštění lokálně

## 1. Vytvoř virtuální prostředí:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

## 2. Nainstaluj zavislosti
```bash
 pip install -r requirements.txt
```
## 3. Spust server
```bash
uvicorn main:app --reload
```

## 4. Otevři dokumentaci v prohlížeči:
```bash
http://127.0.0.1:8000/docs
```
