from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb
from app.database.requests import get_leaderboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)

    await message.answer('Привет! Это бот для запоминания иностранных слов. Нажми /select ' +
                         ', чтобы выбрать язык и начать учить слова.')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Github - ')

@router.message(Command('select'))
async def cmd_start(message: Message):
    keyboard = await kb.translate()
    await message.answer('Выберите язык, который вы будете изучать', reply_markup=keyboard)

@router.message(Command('learn'))
async def cmd_start(message: Message):
    # keyboard = await kb.translate()
    await message.answer('LEARN')


@router.message(Command('leaderboard'))
async def cmd_leaderboard(message: Message):
    top_10 = await get_leaderboard()
    max_name_length = max(len(name) for name in top_10.keys())

    leaderboard_message = "Топ 10 пользователей:\n"
    for index, (name, points) in enumerate(top_10.items(), start=1):
        leaderboard_message += f"{index:<3} {name:<{max_name_length+3}} {points}\n"

    await message.answer(leaderboard_message)


@router.message(Command('tournaments'))
async def cmd_start(message: Message):
    keyboard = await kb.agree()
    await message.answer('TOURNAMENTS', reply_markup=keyboard)