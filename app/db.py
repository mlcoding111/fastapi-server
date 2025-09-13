from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# To change for .env file
DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost/mydb"

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency: get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
