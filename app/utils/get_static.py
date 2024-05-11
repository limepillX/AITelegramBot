import json
from pathlib import Path

from loguru import logger

from app.core.config import config


def _get_static_path() -> Path:
    return config.project_path / "static"


def get_message(lang: str, message: str) -> str:
    messages_path = _get_static_path() / "locales" / lang / "messages.json"
    with open(messages_path, "r") as file:
        messages = json.load(file)

    try:
        return messages[message]
    except KeyError:
        text = f"Message '{message}' not found in '{lang}' locale"
        logger.error(text)
        return text


def get_button(lang: str, button: str) -> str:
    buttons_path = _get_static_path() / "locales" / lang / "buttons.json"
    with open(buttons_path, "r") as file:
        buttons = json.load(file)

    try:
        return buttons[button]
    except KeyError:
        text = f"Button '{button}' not found in '{lang}' locale"
        logger.error(text)
        return text
