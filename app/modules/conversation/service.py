import os
import uuid
import boto3
from boto3.s3.transfer import S3Transfer
from openai import OpenAI
from ...dependencies.aws.aws import get_aws_transfer
from dataclasses import dataclass
from fastapi import Depends
from typing import Annotated
from ..whatsapp.utils import ogg2mp3, send_message
from .repository import ConversationRepository, get_repository
from .schemas import ReceivePayload


@dataclass
class ConversationService:
    repository: ConversationRepository
    s3_transfer: S3Transfer
    client: OpenAI = OpenAI()

    def receive(self, payload: ReceivePayload):
        message_text = payload.body

        if payload.media_url and payload.media_type:
            mp3_file_path = ogg2mp3(payload.media_url)

            with open(mp3_file_path, "rb") as audio_file:
                message_text = self.client.audio.transcriptions.create(
                    file=audio_file, model="whisper-1", language="pt", temperature=0.5
                ).text

                os.remove(mp3_file_path)

        messages = [{"role": "user", "content": message_text}]
        messages.append(
            {
                "role": "system",
                "content": "You're an Portuguese teacher who has taught 100s of students grammar, idioms, vocab, basic Portuguese information, and beyond basics.",
            }
        )
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )

        llm_response = response.choices[0].message.content

        # model = Conversation(
        #     sender=payload.number,
        #     message=message_text,
        #     response=llm_response,
        # )

        # self.repository.create(model)

        if payload.media_url and payload.media_type:
            response = self.client.audio.speech.create(
                model="tts-1", voice="alloy", input=llm_response, response_format="opus"
            )

            file_name = f"{uuid.uuid4()}.opus"
            media_path = f"data/{file_name}"

            response.write_to_file(media_path)

            with self.s3_transfer as s3:
                s3.upload_file(
                    media_path,
                    os.getenv("AWS_BUCKET"),
                    f"audio/{file_name}",
                    extra_args={
                        "ACL": "public-read",
                        "ContentType": "audio/ogg",
                    },
                )

                os.remove(media_path)

                s3_file_path = f"http://{os.getenv('AWS_BUCKET')}.s3.{os.getenv('AWS_DEFAULT_REGION')}.amazonaws.com/audio/{file_name}"

                send_message(payload.number, llm_response, s3_file_path)

        else:
            send_message(payload.number, llm_response, None)

        return True


def get_service(
    repository: Annotated[ConversationRepository, Depends(get_repository)],
    s3_transfer: Annotated[S3Transfer, Depends(get_aws_transfer)],
) -> ConversationService:
    return ConversationService(repository, s3_transfer)
