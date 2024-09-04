from tkinter.tix import Select
from typing import Coroutine, Tuple, Any
from sqlalchemy import BigInteger
from sqlalchemy import select, func, update, Select
from sqlalchemy.orm import selectinload

from app.database.models import User, Word, Leaderboard


# возвращает пользователя по tg_id
def select_tgid_user(tg_id):
    return select(User).where(User.tg_id == tg_id)


# add user
def create_user(tg_id):
    return User(tg_id=tg_id)


# выбирает оригинал и перевод с учетом dif
def select_word_diff(diff):
    return select(Word).where(Word.difficulty == diff).order_by(func.random()).limit(1)


# выбирает оригинал и перевод без учета dif
def select_word():
    return select(Word).order_by(func.random()).limit(1)


# выбирает 3 случайных значения с учетом dif
def select_3word_diff(column):
    return select(column).order_by(func.random()).limit(3)


# выбирает 3 случайных значения без учета dif
def select_3word(column):
    return select(column).order_by(func.random()).limit(3)


# проверка пользователя в leaderboard
def check_user_leaderboard(tg_id):
    return select(Leaderboard).where(Leaderboard.tg_id == tg_id)


# обновление очков и имени пользователя
def update_user_points(tg_id, points, name):
    return update(Leaderboard).where(Leaderboard.tg_id == tg_id).values(point=points, name=name)


# добавление нового пользователя в leaderboard
def create_leaderboard(tg_id, points, name):
    return Leaderboard(tg_id=tg_id, name=name, point=points)


# выбирает топ 10 лидеров
def select_leaderboard():
    return select(Leaderboard).order_by(Leaderboard.point.desc()).limit(10)
