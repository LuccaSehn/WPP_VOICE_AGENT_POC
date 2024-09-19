from fastapi import Depends, APIRouter, Request, HTTPException
from typing import Annotated
from .service import ConversationService, get_service
from .schemas import ReceivePayload

router = APIRouter(prefix="/conversation", tags=["conversation"])


@router.post("/webhook")
async def reply(
    request: Request, service: Annotated[ConversationService, Depends(get_service)]
):
    form_data = await request.form()

    whatsapp_number = form_data["From"].split("whatsapp:")[-1]

    payload = ReceivePayload(
        number=whatsapp_number,
        body=form_data["Body"],
        media_url=form_data.get("MediaUrl0", None),
        media_type=form_data.get("MediaContentType0", None),
    )

    try:
        res = service.receive(payload)
        if res == None:
            raise HTTPException(400, "Error to process audio.")
        return res
    except Exception as e:
        print(f"error: {e}")
        raise HTTPException(500, "Internal error.")
