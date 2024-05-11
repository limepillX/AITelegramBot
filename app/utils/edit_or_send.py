from aiogram import types
from aiogram.exceptions import AiogramError
from loguru import logger

from app.core.loader import bot


async def edit_or_send(message: types.Message, text: str, **kwargs):
    if message.text == text:
        return
    try:
        await message.edit_text(text, **kwargs)

    except AiogramError:
        logger.error(f"Error while editing message: {message.message_id}. Sending new message.")
        await bot.send_message(message.chat.id, text, **kwargs)
