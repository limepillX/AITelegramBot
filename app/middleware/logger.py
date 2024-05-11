from typing import Any, Awaitable, Callable, Dict

from aiogram import types
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from loguru import logger


class LoggerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any],
    ) -> Any:
        if type(event) is types.Message:
            text = event.text
        elif type(event) is types.CallbackQuery:
            text = event.data

        if user := event.from_user:
            message = "{username}/{id}: {text}".format(username=user.username, id=user.id, text=text)
            logger.info(message)

        return await handler(event, data)
