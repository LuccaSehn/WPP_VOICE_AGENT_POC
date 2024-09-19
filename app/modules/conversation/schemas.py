from pydantic import BaseModel, Field
from faker import Faker

fake = Faker()


class ReceivePayload(BaseModel):
    number: str = Field(examples=[fake.phone_number()])
    media_url: str | None = Field(examples=[fake.url()])
    media_type: str | None = Field(examples=["asda"])
    body: str = Field(examples=["asda"])
