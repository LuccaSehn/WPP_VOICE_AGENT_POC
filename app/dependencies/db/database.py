from sqlalchemy.orm import Session
from typing import Generator
from contextlib import contextmanager
from .config import SessionLocal


@contextmanager
def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
