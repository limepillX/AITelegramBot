import asyncio

from loguru import logger

from app.core.loader import bot, dp
from app.middleware import LoggerMiddleware

dp.message.middleware(LoggerMiddleware())  
dp.callback_query.middleware(LoggerMiddleware())

if __name__ == "__main__":
    logger.debug("Starting bot...")
    __import__("app.handlers")

    logger.success("Bot started")
    asyncio.run(dp.start_polling(bot))
