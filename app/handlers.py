from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    keyboard = await kb.original()
    await message.answer("PRIV", reply_markup=keyboard)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('this is /help')


@router.message(F.text == 'How')
async def cmd_how(message: Message):
    await message.answer('ok')

@router.message(Command('select'))
async def cmd_start(message: Message):
    keyboard = await kb.translate()
    await message.answer('Выберите язык, который вы будете изучать', reply_markup=keyboard)
