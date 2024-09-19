import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from .config import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    sender = Column(String, nullable=False)
    message = Column(String, nullable=False)
    response = Column(String, nullable=False)
