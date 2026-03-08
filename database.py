from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+psycopg2://neondb_owner:npg_LYUn7RhqV2sy@ep-weathered-queen-ai35cf7f-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# 👇 ESTA ES LA FUNCIÓN QUE TE FALTA
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()