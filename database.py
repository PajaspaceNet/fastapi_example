from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(str(DATABASE_URL).replace("+aiosqlite", ""), echo=True)

