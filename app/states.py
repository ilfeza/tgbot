from aiogram.fsm.state import StatesGroup, State


class Learning(StatesGroup):
    original = State()
    translation = State()
    difficulty = State()

    orig_lang = State()
    transl_lang = State()

    in_study = State()


