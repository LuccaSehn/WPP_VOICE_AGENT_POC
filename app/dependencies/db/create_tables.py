from config import engine, Base
from models import Conversation

Base.metadata.create_all(bind=engine)
