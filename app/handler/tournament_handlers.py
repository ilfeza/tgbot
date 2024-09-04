from aiogram import F, Router
from aiogram.fsm import state
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.database.requests as rq
from app.database.requests import add_user_points
from app.states import Learning
from aiogram.fsm.context import FSMContext
from app.services import lang, get_translations

router = Router()


async def update_state_tournament(state: FSMContext, message, orig_value, transl_value, translation, keyboard):
    await state.set_state(Learning.orig_lang)
    await state.update_data(orig_lang=orig_value)

    await state.set_state(Learning.transl_lang)
    await state.update_data(transl_lang=transl_value)

    await message.answer(orig_value, reply_markup=keyboard)

    await state.set_state(Learning.in_tournament)
@router.callback_query(F.data.startswith('agree_'))
async def start_tournament(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Learning.difficulty)
    await state.update_data(difficulty=0)

    # Получить клавиатуру по state
    user_state = await state.get_data()
    orig_value, transl_value, translation = await get_translations(user_state.get("original"),
                                                                   user_state.get("translation"),
                                                                   user_state.get("difficulty"))

    keyboard = await kb.learning(translation)

    await update_state_tournament(state, callback.message, orig_value, transl_value, translation, keyboard)

    await state.update_data(in_tournament=0)


@router.message(Learning.in_tournament)
async def translate(message: Message, state: FSMContext):
    user_state = await state.get_data()

    if message.text == user_state.get("transl_lang"):
        points = user_state.get("in_tournament") + 1
        await state.update_data(in_tournament=points)

        # print(user_state)
        await message.answer('Все верно')
    else:
        await add_user_points(message.from_user.id, message.from_user.full_name, user_state.get("in_tournament"))
        await state.update_data(in_tournament=0)
        await message.answer('Не верно, правильно ' + str(user_state.get("transl_lang")))

    orig_value, transl_value, translation = await get_translations(user_state.get("original"),
                                                                   user_state.get("translation"),
                                                                   user_state.get("difficulty"))

    keyboard = await kb.learning(translation)

    await update_state_tournament(state, message, orig_value, transl_value, translation, keyboard)
