import asyncio

import aiofiles
import aiohttp
from aiogram import types
from aiogram.fsm.context import FSMContext
from loguru import logger
from openai import APIError

from app import callbacks, keyboards, services, states, utils
from app.core.config import config
from app.core.loader import bot


async def _save_image_task(folder_name: str, file_name: str, url: str, session: aiohttp.ClientSession) -> None:
    path = config.project_path / "static" / "images" / folder_name / file_name
    path.parent.mkdir(parents=True, exist_ok=True)
    async with session.get(url) as response:
        async with aiofiles.open(path, "wb") as file:
            await file.write(await response.read())


async def _save_images(folder_name: str, file_name: str, response: list[str]) -> None:
    tasks = []

    async with aiohttp.ClientSession() as session:
        for url in response:
            tasks.append(_save_image_task(folder_name, file_name, url, session))
        await asyncio.gather(*tasks)


async def generate_dalle_image(prompt: str | None, message: types.Message, user: types.User, state: FSMContext):
    user_language = user.language_code or "en"
    if not prompt:
        await message.answer(utils.get_message(user_language, "dalle_no_prompt"))
        await state.set_state(states.WaitForPrompt.dalle)
        return

    processing_message = await message.answer(
        utils.get_message(user_language, "dalle_processing").format(prompt=prompt)
    )
    await bot.send_chat_action(message.chat.id, "upload_photo")

    try:
        image_urls = await services.get_dalle_response(prompt)

        folder_name = f"{user.username or user.id}"
        file_name = f"{prompt}-{message.message_id}.jpg"
        await _save_images(folder_name, file_name, image_urls)
    except APIError as e:
        error_text = utils.get_message(user_language, "error").format(error_text=e)
        await utils.edit_or_send(processing_message, error_text)
        logger.error(str(e))
        return

    result_text = utils.get_message(user_language, "dalle_result").format(prompt=message.text)
    keyboard = keyboards.RegenerateImage(user_language).build(callbacks.MainMenu().pack())
    if len(image_urls) > 1:
        await message.answer_media_group([types.InputMediaPhoto(media=url) for url in image_urls])
        await message.answer(result_text, reply_markup=keyboard)
    else:
        await message.answer_photo(image_urls[0], caption=result_text, reply_markup=keyboard)

    await processing_message.delete()
    await state.set_state(None)
