from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .modules.conversation.routes import router as conversation_router

load_dotenv()

app = FastAPI()

app.include_router(conversation_router)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/health", include_in_schema=False)
async def health():
    return "ok"
