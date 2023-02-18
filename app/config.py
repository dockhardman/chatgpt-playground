import logging
from typing import Text

from pydantic import BaseSettings


class Settings(BaseSettings):
    # General
    logger_name: Text = (
        "uvicorn.error"
        if "uvicorn.error" in logging.root.manager.loggerDict
        else "chatgpt"
    )

    # ChatGPT Config
    chatgpt_email: Text = ""
    chatgpt_password: Text = ""
    chatgpt_paid: bool = False


settings = Settings()
logger = logging.getLogger(settings.logger_name)
