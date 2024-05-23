from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states.anketa import Anketa
from keyboards.anketa import *

router = Router()

@router.message (Command("game"))
async def anketa_handler(msg: Message, state: FSMContext):
    '''aa'''
    await state.set_state(Anketa.name)
    await msg.answer('Введите Ваш никнейм', reply_markup=kb_apteka_cancel)

@router.callback_query(F.data == 'cancel_anketa')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext):
    '''jhgf'''
    await state.clear()
    await callback_query.message.answer ("Регистрация отменена")

@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    '''nbv'''
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    await msg.answer ('Введите возраст', reply_markup=kb_apteka_cancel_and_back)

@router.callback_query(F.data == 'back_anketa')
async def back_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    '''321'''
    current_state = await state.get_state()
    if current_state == Anketa.gender:
        await state.set_state(Anketa.age)
        await callback_query.message.answer('Введите Ваш возраст', reply_markup=kb_apteka_cancel_and_back)
    elif current_state == Anketa.age:
        await state.set_state(Anketa.name)
        await callback_query.message.answer('Введите Ваше имя', reply_markup=kb_apteka_cancel)
@router.message (Anketa.age)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    '''liu'''
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer ('Вы не верно ввели возраст!')
        await msg.answer('Введите Ваш возраст', reply_markup=kb_apteka_cancel_and_back)
        return
    await state.set_state(Anketa.gender)    
    await msg.answer(
        'Выберите игру',
        reply_markup=kb_apteka_by_gender)

@router.callback_query(F.data.startswith('game_') and Anketa.gender)
async def set_game_handler(callback_query: CallbackQuery, state: FSMContext):
    '''Выбор игры'''
    game = {'game_cs2': 'CS2',
            'game_dota2': 'DOTA2',
            'game_WOT': 'World of Tanks',
            'game_Valorant': 'Valorant',
            'game_PUBG': 'PUBG',
            'game_Heartstone': 'Heartstone'}[callback_query.data]
    await state.update_data(game=game)
    await callback_query.message.answer(str(await state.get_data()))
    await state.clear()

@router.message(Anketa.gender)
async def set_game_by_handler(msg: Message, state: FSMContext):
    await msg.answer('Выберите игру')

