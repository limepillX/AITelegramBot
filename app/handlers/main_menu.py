from aiogram import F, types
from aiogram.filters import Command

from app import callbacks, services
from app.core.loader import dp


@dp.message(Command("start"))
async def start(message: types.Message):
    if message.from_user is None:
        return

    await services.send_start_message(message, message.from_user)

@dp.callback_query(callbacks.MainMenu().filter())
async def main_menu(callback: types.CallbackQuery, callback_data: callbacks.MainMenu):
    if type(callback.message) is not types.Message:
        return
    
    await services.send_start_message(callback.message, callback.from_user, edit=callback_data.edit_last)