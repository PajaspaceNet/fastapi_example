from databases import Database
from sqlalchemy import create_engine, MetaData

# Připojení k PostgreSQL
DATABASE_URL = "postgresql+asyncpg://postgres:heslo@localhost:5432/mydb"


database = Database(DATABASE_URL)
metadata = MetaData()

# SQLAlchemy engine (pozor: bez asyncpg v názvu!)
engine = create_engine(str(DATABASE_URL).replace("+asyncpg", ""), echo=True)
