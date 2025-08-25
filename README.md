


<img width="246" height="244" alt="logo" src="https://github.com/user-attachments/assets/7e2d6812-059d-42ab-9e48-1efa2bf735c9" />



# fastapi_example

Project example fastapi  REST API v Pythonu + FastAPI <br>
Jednoduchy projekt -  REST API pro správu úkolů v Pythonu + FastAPI + SQLite.

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

## 3. Stazeni projekt z GituHubu 

Pokud chcete projekt získat z GitHubu, můžete použít příkaz:

```bash
git clone https://github.com/PajaspaceNet/fastapi_example.git
cd fastapi_example
```

## 4. Nainstaluj zavislosti
```bash
 pip install -r requirements.txt
```
## 5. Spust server
```bash
uvicorn main:app --reload
```

## 6. Otevři dokumentaci v prohlížeči:
```bash
http://127.0.0.1:8000/docs
```
