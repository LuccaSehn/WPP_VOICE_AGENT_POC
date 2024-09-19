import logging
import os
import uuid
import requests
import urllib.request
from twilio.rest import Client
from pydub import AudioSegment

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = os.getenv("TWILIO_FROM_NUMBER")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_message(to_number, body_text, media_path):
    try:
        if media_path:
            message = client.messages.create(
                from_=f"whatsapp:{twilio_number}",
                to=f"whatsapp:{to_number}",
                media_url=[media_path],
                send_as_mms=True,
            )
        else:
            message = client.messages.create(
                from_=f"whatsapp:{twilio_number}",
                body=body_text,
                to=f"whatsapp:{to_number}",
            )
        logger.info(f"Message sent to {to_number}: {message.body}")
    except Exception as e:
        logger.error(f"Error sending message to {to_number}: {e}")


def ogg2mp3(audio_url):
    # Get the response of the OGG file
    response = requests.get(audio_url)
    # Get the redirect URL result
    url = response.url
    file_name = uuid.uuid4()
    # Download the OGG file
    urllib.request.urlretrieve(url, f"data/{file_name}.ogg")
    # Load the OGG file
    audio_file = AudioSegment.from_ogg(f"data/{file_name}.ogg")
    # Export the file as OGG
    audio_file.export(f"data/{file_name}.ogg", format="ogg")
    return os.path.join(os.getcwd(), f"data/{file_name}.ogg")
