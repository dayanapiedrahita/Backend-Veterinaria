import os
from dotenv import load_dotenv

# Cargar variables de entorno de prueba
load_dotenv()

# Asegurar que hay una DATABASE_URL para tests
if not os.getenv("DATABASE_URL"):
    os.environ["DATABASE_URL"] = "sqlite:///./test.db"
