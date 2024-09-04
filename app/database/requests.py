from app.database.models import async_session
from app.database.crud import *

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select_tgid_user(tg_id))

        if not user:
            session.add(create_user(tg_id))
            await session.commit()


async def get_leaderboard() -> dict:
    async with async_session() as session:
        # query = select(Leaderboard).order_by(Leaderboard.point.desc()).limit(10)
        result = await session.execute(select_leaderboard())
        top_10 = result.scalars().all()

        top_10_dict = {entry.name: entry.point for entry in top_10}
        return top_10_dict

async def get_orig_transl(orig, transl, diff):
    async with async_session() as session:

        if diff == 0:
            result = await session.execute(
                select_word()
            )
        else:
            result = await session.execute(
                select_word_diff(diff)
            )

        word_instance = result.scalar_one()

        orig_value = getattr(word_instance, orig)
        transl_value = getattr(word_instance, transl)

        return orig_value, transl_value

# если не указана сложность, то она не учитывается
async def get_random_values(transl, diff):
    async with async_session() as session:
        column = getattr(Word, transl)

        if diff == 0:
            result = await session.execute(
                select_3word(column)
            )
        else:
            result = await session.execute(
                select_3word_diff(column)
            )

        values = result.scalars().all()

        return values


async def add_user_points(tg_id: int, name: str, points: int):
    async with async_session() as session:
        result = await session.execute(
            check_user_leaderboard(tg_id)
        )
        user = result.scalar_one_or_none()

        if user:
            if points > user.point:
                await session.execute(update_user_points(tg_id, points, name))
        else:
            session.add(create_leaderboard(tg_id, points, name))

        await session.commit()
