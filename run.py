import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handler import other_handlers, handlers, tournament_handlers
from app.database.models import async_main

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(handlers.router)
    dp.include_router(other_handlers.router)
    dp.include_router(tournament_handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
