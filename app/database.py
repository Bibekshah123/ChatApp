from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://chatuser:chatpass@localhost/chatdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,  autocommit=False, autoflush=False)

Base = declarative_base()
