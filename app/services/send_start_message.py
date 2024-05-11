from aiogram import types
from aiogram.exceptions import TelegramBadRequest

from app import keyboards, utils
from app.core.config import config


async def send_start_message(message: types.Message, user: types.User, edit: bool = False):
    user_language = user.language_code or "en"
    keyboard = keyboards.StartKeyboard(language=user_language)
    text = utils.get_message(user_language, "start").format(
        gpt=config.openai.gpt.model.upper(), dalle=config.openai.dalle.model.upper()
    )
    if edit:
        await utils.edit_or_send(message, text, reply_markup=keyboard.build())
    else:
        try:
            await message.edit_reply_markup()
        except TelegramBadRequest:
            pass
        await message.answer(text, reply_markup=keyboard.build())
