from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery
from keyboards.start import *
from aiogram.fsm.context import FSMContext
router = Router()

@router.message (Command("start"))
async def start_handler(msg: Message):
    '''h'''
    from main import bot
    await bot.set_my_commands ([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='anketa', description= 'Справка'),
        BotCommand(command='game', description= 'Выбрать игру'),
        BotCommand(command='time_zone', description= 'Выбрать часовой пояс'),
        BotCommand(command='time', description= 'Выбрать время'),
        BotCommand(command='nickname', description= 'Написать ник'),
        ])
    await msg.answer (text = "Привет! Я помогу тебе найти лучшего напарника для совместной игры. От тебя мне потребуется всего лишь знать во что ты играешь, когда и в какой день. Напиши /game для выбора игры.", reply_markup=kb_start_next)

@router.message (Command("start"))
async def start_game(msg: Message, state: FSMContext):
