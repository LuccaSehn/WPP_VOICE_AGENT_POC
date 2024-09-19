from dataclasses import dataclass
from typing import Annotated, Generator
from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from ...dependencies.db.database import get_db
from ...dependencies.db.models import Conversation


@dataclass
class ConversationRepository:
    db: Generator[Session, None, None]

    def create(self, model: Conversation):
        try:
            conversation = Conversation(
                sender=model.sender,
                message=model.message,
                response=model.message,
            )
            self.db.add(conversation)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()


def get_repository(
    db: Annotated[Generator[Session, None, None], Depends(get_db)]
) -> ConversationRepository:
    return ConversationRepository(db)
