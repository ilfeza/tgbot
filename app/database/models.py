from sqlalchemy import BigInteger, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)


class Word(Base):
    __tablename__ = 'words'
    id: Mapped[int] = mapped_column(primary_key=True)
    english: Mapped[str] = mapped_column(String(50))
    russian: Mapped[str] = mapped_column(String(50))
    korean: Mapped[str] = mapped_column(String(50))
    difficulty: Mapped[int] = mapped_column(Integer, default=1)

class Leaderboard(Base):
    __tablename__ = 'leaderboards'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.tg_id'))
    name: Mapped[str] = mapped_column(String(50))
    point: Mapped[int] = mapped_column(Integer, default=0)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
