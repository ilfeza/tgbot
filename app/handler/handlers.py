from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb
import app.database.requests as rq

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

@router.message(Command('tournament'))
async def cmd_start(message: Message):

    await message.answer('TOURNAMENT')

@router.message(Command('leaderboard'))
async def cmd_start(message: Message):
    keyboard = await kb.agree()
    await message.answer('LEADERBOARD', reply_markup=keyboard)