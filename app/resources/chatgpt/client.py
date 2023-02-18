from typing import Dict, Optional, Text, Tuple

from revChatGPT.V1 import Chatbot as ChatGPTChatbot

from app.config import logger, settings


if not settings.chatgpt_email:
    logger.warning("ChatGPT email 'chatgpt_email' not set.")
if not settings.chatgpt_password:
    logger.warning("ChatGPT password 'chatgpt_password' not set.")


class ChatGptClient:
    _client_pool: Dict[Tuple[Text, Text, bool], "ChatGPTChatbot"] = {}

    @classmethod
    def get_default_chatgpt_client(cls) -> "ChatGPTChatbot":
        return cls.get_chatgpt_client(
            email=settings.chatgpt_email,
            password=settings.chatgpt_password,
            paid=settings.chatgpt_paid,
        )

    @classmethod
    def get_chatgpt_client(
        cls,
        email: Optional[Text],
        password: Text,
        paid: bool,
    ) -> "ChatGPTChatbot":
        config_key = (email, password, paid)
        if config_key in cls._client_pool:
            return cls._client_pool[config_key]
        else:
            _client = ChatGPTChatbot(
                config=dict(email=email, password=password, paid=paid)
            )
            cls._client_pool[config_key] = _client
            return _client
