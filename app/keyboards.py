from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='catalog')],
    [KeyboardButton(text='trash'), KeyboardButton(text='contact')]
],
    resize_keyboard=True,
    input_field_placeholder='Select menu')

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
    return keyboard.adjust(2).as_markup()