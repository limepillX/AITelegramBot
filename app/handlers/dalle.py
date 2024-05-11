from aiogram import types
from aiogram.fsm.context import FSMContext

from app import callbacks, keyboards, services, states, utils
from app.core.loader import dp


@dp.callback_query(callbacks.AskDALLE().filter())
async def ask_dalle(callback: types.CallbackQuery, state: FSMContext):
    if type(callback.message) is not types.Message:
        return

    user_language = callback.from_user.language_code or "en"
    keyboard = keyboards.BaseKeyboard(user_language).build(callbacks.MainMenu(edit_last=True).pack())
    await utils.edit_or_send(callback.message, utils.get_message(user_language, "ask_dalle"), reply_markup=keyboard)
    await state.set_state(states.WaitForPrompt.dalle)


@dp.message(states.WaitForPrompt.dalle)
async def dalle_prompt(message: types.Message, state: FSMContext):
    if not message.from_user or not message.text:
        return
    await state.update_data(prompt=message.text)

    await services.generate_dalle_image(message.text, message, message.from_user, state)


@dp.callback_query(callbacks.RegenerateImage().filter())
async def regenerate_image(callback: types.CallbackQuery, state: FSMContext):
    if type(callback.message) is not types.Message:
        return

    state_data = await state.get_data()
    if callback.message.reply_markup:
        await callback.message.edit_reply_markup()
        
    await services.generate_dalle_image(state_data.get("prompt"), callback.message, callback.from_user, state)
