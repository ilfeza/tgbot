from aiogram import F, Router
from aiogram.fsm import state
from aiogram.types import Message
from aiogram.types import CallbackQuery

import app.keyboards as kb
import app.database.requests as rq
from app.states import Learning
from aiogram.fsm.context import FSMContext
from app.services import lang, get_translations

router = Router()


@router.callback_query(F.data.startswith('translate_'))
async def select_translate(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Learning.translation)
    await state.update_data(translation=callback.data.split('_')[1])
    a = await state.get_data()
    print(a["translation"])

    keyboard = await kb.original()
    await callback.message.edit_text('Выберите язык, который вы знаете', reply_markup=keyboard)

@router.callback_query(F.data.startswith('original_'))
async def select_original(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Learning.original)
    await state.update_data(original=callback.data.split('_')[1])
    a = await state.get_data()
    print(a["original"])

    selected_language = lang.get(a["original"].lower())
    translated_to = lang.get(a["translation"].lower())

    await callback.message.edit_text(
        f'Вы выбрали:\n'
        f'Оригинал: {selected_language}\n'
        f'Перевод: {translated_to}'
    )


    orig_value, transl_value, translation = await get_translations(a["original"], a["translation"])

    await state.set_state(Learning.orig_lang)
    await state.update_data(orig_lang=orig_value)

    await state.set_state(Learning.transl_lang)
    await state.update_data(transl_lang=transl_value)

    keyboard = await kb.learning(translation)

    await callback.message.answer(orig_value, reply_markup=keyboard)
    await state.set_state(Learning.in_study)
    await state.update_data(in_study=True)

@router.message(Learning.in_study)
async def translate(message: Message, state: FSMContext):
    a = await state.get_data()
    print(a)
    print(a["transl_lang"])
    print(message)
    if message.text == a["transl_lang"]:
        await message.answer('Все верно')



    else:
        print(a)
        await message.answer('Не верно, правильно ' + str(a["transl_lang"]))

    orig_value, transl_value, translation = await get_translations(a["original"], a["translation"])

    await state.set_state(Learning.orig_lang)
    await state.update_data(orig_lang=orig_value)

    await state.set_state(Learning.transl_lang)
    await state.update_data(transl_lang=transl_value)

    keyboard = await kb.learning(translation)

    await message.answer(orig_value, reply_markup=keyboard)

    await state.set_state(Learning.in_study)
    await state.update_data(in_study=True)