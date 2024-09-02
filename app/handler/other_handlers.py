from aiogram import F, Router
from aiogram.fsm import state
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.database.requests as rq
from app.states import Learning
from aiogram.fsm.context import FSMContext
from app.services import lang, get_translations, update_state_learning

router = Router()


# выбор orig языка
@router.callback_query(F.data.startswith('translate_'))
async def select_translate(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Learning.translation)
    await state.update_data(translation=callback.data.split('_')[1])
    a = await state.get_data()
    print(a["translation"])

    keyboard = await kb.original()
    await callback.message.edit_text('Выберите язык, который вы знаете', reply_markup=keyboard)


# вывод dif языка
@router.callback_query(F.data.startswith('original_'))
async def select_original(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Learning.original)
    await state.update_data(original=callback.data.split('_')[1])
    a = await state.get_data()
    print(a["original"])

    keyboard = await kb.difficulty()
    await callback.message.edit_text('Выберите сложность', reply_markup=keyboard)


# вывод выбора
@router.callback_query(F.data.startswith('difficulty_'))
async def select_difficulty(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Learning.difficulty)
    await state.update_data(difficulty=callback.data.split('_')[1])
    user_state = await state.get_data()

    selected_language = lang.get(user_state.get("original"))
    translated_to = lang.get(user_state.get("translation"))
    diff = user_state.get("difficulty")

    await callback.message.edit_text(
        f'Вы выбрали:\n'
        f'Оригинал: {selected_language}\n'
        f'Перевод: {translated_to}\n'
        f'Сложность: {diff}'
    )

    orig_value, transl_value, translation = await get_translations(user_state.get("original"),
                                                                   user_state.get("translation"),
                                                                   user_state.get("difficulty"))

    keyboard = await kb.learning(translation)

    await update_state_learning(state, callback.message, orig_value, transl_value, translation, keyboard)


@router.message(Learning.in_study)
async def translate(message: Message, state: FSMContext):
    user_state = await state.get_data()

    if message.text:
        if message.text == user_state.get("transl_lang"):
            await message.answer('Все верно')
        else:
            await message.answer('Не верно, правильно ' + str(user_state.get("transl_lang")))

    orig_value, transl_value, translation = await get_translations(user_state.get("original"),
                                                                   user_state.get("translation"),
                                                                   user_state.get("difficulty"))

    keyboard = await kb.learning(translation)

    await update_state_learning(state, message, orig_value, transl_value, translation, keyboard)
