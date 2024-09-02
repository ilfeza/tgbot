import random

from app.database.requests import *
from app.states import Learning
from aiogram.fsm.context import FSMContext

lang = {'russian': 'Русский',
        'english': 'Английский',
        'korean': 'Корейский'}


async def get_translations(orig, transl, diff):
    orig_value, transl_value = await get_orig_transl(orig, transl, diff)
    translation = await get_random_values(transl, diff)

    translation.append(transl_value)

    random.shuffle(translation)

    return orig_value, transl_value, translation

async def update_state_learning(state: FSMContext, message, orig_value, transl_value, translation, keyboard):
    await state.set_state(Learning.orig_lang)
    await state.update_data(orig_lang=orig_value)

    await state.set_state(Learning.transl_lang)
    await state.update_data(transl_lang=transl_value)

    await message.answer(orig_value, reply_markup=keyboard)

    await state.set_state(Learning.in_study)
    await state.update_data(in_study=True)

async def update_state_tournament(state: FSMContext, message, orig_value, transl_value, translation, keyboard):
    await state.set_state(Learning.orig_lang)
    await state.update_data(orig_lang=orig_value)

    await state.set_state(Learning.transl_lang)
    await state.update_data(transl_lang=transl_value)

    await message.answer(orig_value, reply_markup=keyboard)

    await state.set_state(Learning.in_tournament)