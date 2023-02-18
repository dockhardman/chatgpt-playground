from typing import Optional, Text

from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse

from app.config import logger
from app.resources.chatgpt.client import ChatGptClient, ChatGPTChatbot


router = APIRouter()


@router.post("/conversation")
async def conversation(
    message: Text,
    conversation_id: Optional[Text] = None,
    parent_id: Optional[Text] = None,
    chatbot: ChatGPTChatbot = Depends(ChatGptClient.get_default_chatgpt_client),
):
    """ChatGPT conversation endpoint."""

    try:
        responses = [response for response in chatbot.ask(message)]
    except Exception as e:
        logger.exception(e)
        return PlainTextResponse(str(e))

    return PlainTextResponse(responses[-1]["message"])
