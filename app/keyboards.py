from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='catalog')],
    [KeyboardButton(text='trash'), KeyboardButton(text='contact')]
],
    resize_keyboard=True,
    input_field_placeholder='Select menu')


# orig язык
async def original() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='Русский', callback_data=f"original_{'russian'}"),
        InlineKeyboardButton(text='Английский', callback_data=f"original_{'english'}"),
        InlineKeyboardButton(text='Корейский', callback_data=f"original_{'korean'}")
    )
    keyboard.add(
        InlineKeyboardButton(text='На главную', callback_data='to_main')
    )

    return keyboard.adjust(1).as_markup()


# transl язык
async def translate() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='Русский', callback_data=f"translate_{'russian'}"),
        InlineKeyboardButton(text='Английский', callback_data=f"translate_{'english'}"),
        InlineKeyboardButton(text='Корейский', callback_data=f"translate_{'korean'}")
    )
    keyboard.add(
        InlineKeyboardButton(text='На главную', callback_data='to_main')
    )

    return keyboard.adjust(1).as_markup()


async def learning(words):
    keyboard = ReplyKeyboardBuilder()
    for word in words:
        keyboard.add(KeyboardButton(text=word))

    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard.adjust(2).as_markup().keyboard,
        resize_keyboard=True,
        input_field_placeholder='Select menu'
    )

    return reply_keyboard

async def return_main():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='На главную', callback_data='to_main')
    )

    return keyboard.adjust(1).as_markup()


# сложность языка
async def difficulty() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='1', callback_data=f"difficulty_{'1'}"),
        InlineKeyboardButton(text='2', callback_data=f"difficulty_{'2'}"),
        InlineKeyboardButton(text='3', callback_data=f"difficulty_{'3'}"),
        InlineKeyboardButton(text='4', callback_data=f"difficulty_{'4'}"),
        InlineKeyboardButton(text='5', callback_data=f"difficulty_{'5'}"),
        InlineKeyboardButton(text='6', callback_data=f"difficulty_{'6'}")
    )
    keyboard.add(
        InlineKeyboardButton(text='На главную', callback_data='to_main')
    )

    return keyboard.adjust(3).as_markup()

async def agree():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='Я согласен', callback_data='agree_')
    )

    return keyboard.adjust(1).as_markup()