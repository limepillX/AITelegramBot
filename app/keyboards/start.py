from app import callbacks
from app.keyboards.base_keyboard import BaseKeyboard


class StartKeyboard(BaseKeyboard):
    def _build(self) -> None:
        self.add(
            self._get_button("ask_chatgpt", callbacks.AskChatGPT().pack()),
            self._get_button("ask_dalle", callbacks.AskDALLE().pack()),
        )
        self.adjust(1)
