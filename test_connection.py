from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()  # carga tu .env

engine = create_engine(os.getenv("DATABASE_URL"))
conn = engine.connect()
print("Conexión OK a Neon")
conn.close()