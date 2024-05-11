from aiogram.fsm.state import State, StatesGroup


class WaitForPrompt(StatesGroup):
    gpt = State()
    dalle = State()
