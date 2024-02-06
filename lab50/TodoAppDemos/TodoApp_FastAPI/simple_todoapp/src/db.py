from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database connection configuration
DB_URL = "sqlite:///./db.sqlite"  # SQLite database file path

# Create SQLAlchemy engine for database interaction
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class for managing database sessions
SessionLocal = sessionmaker(
    autocommit=False,  # Disable autocommit to control transactions manually
    autoflush=False,   # Disable autoflush to control flushing behavior
    bind=engine        # Bind the session to the engine
)

# Base class for declarative model definitions
Base = declarative_base()
