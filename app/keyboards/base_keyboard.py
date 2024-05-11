from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app import utils


class BaseKeyboard(InlineKeyboardBuilder):
    def __init__(self, language: str, *args, **kwargs):
        """
        Base keyboard class

        :param language: User language
        :param *args: args
        :param **kwargs: kwargs
        """
        super().__init__(*args, **kwargs)
        self.language = language

    def _get_button(self, button_name: str, callback_data: str | None = None) -> InlineKeyboardButton:
        return InlineKeyboardButton(
            text=utils.get_button(self.language, button_name), callback_data=callback_data or button_name
        )

    def _build(self) -> None:
        pass

    def build(self, back_callback: str | None = None) -> InlineKeyboardMarkup:
        if back_callback:
            self.add(self._get_button("back", back_callback))
        self._build()
        return self.as_markup()