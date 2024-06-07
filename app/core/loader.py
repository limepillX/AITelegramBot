from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from openai import AsyncOpenAI

from app.core.config import config

bot = Bot(token=config.bot_token)

bot = Bot(token=config.telegram_bot.token, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

openai_client = AsyncOpenAI(api_key=config.openai.api_key)
