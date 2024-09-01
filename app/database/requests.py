from app.database.models import async_session
from app.database.models import User, Word
from sqlalchemy import select, func


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_orig_transl(orig, transl, diff):
    async with async_session() as session:
        result = await session.execute(
            select(Word).where(Word.difficulty == diff).order_by(func.random()).limit(1)
        )
        word_instance = result.scalar_one()

        orig_value = getattr(word_instance, orig)
        transl_value = getattr(word_instance, transl)

        return orig_value, transl_value


async def get_random_values(transl, diff):
    async with async_session() as session:
        column = getattr(Word, transl)

        result = await session.execute(
            select(column).where(Word.difficulty == diff).order_by(func.random()).limit(3)
        )

        values = result.scalars().all()

        return values
