from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not configured in environment or .env file")

engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    print("Conexión OK a la base de datos")
