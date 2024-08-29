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
    await message.answer('this is /help')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Github - ')

# выбор transl языка
@router.message(Command('select'))
async def cmd_start(message: Message):
    keyboard = await kb.translate()
    await message.answer('Выберите язык, который вы будете изучать', reply_markup=keyboard)
