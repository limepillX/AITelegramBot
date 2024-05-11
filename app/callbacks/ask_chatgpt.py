from aiogram.filters.callback_data import CallbackData


class AskChatGPT(CallbackData, prefix="ask_gpt"):
    with_cache: bool | None = None
