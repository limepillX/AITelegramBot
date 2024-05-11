from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from app import callbacks
from app.keyboards.base_keyboard import BaseKeyboard


class RegenerateImage(BaseKeyboard):
    def _build(self) -> None:
        self.add(self._get_button("regenerate_image", callbacks.RegenerateImage().pack()))
        self.adjust(1)
