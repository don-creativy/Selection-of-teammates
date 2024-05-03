from aiogram import Router
from aiogram.filters import Command
from aiogram.types import BotCommand, Message
from aiogram.fsm.context import FSMContext

from main import bot 

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await bot.set_my_commands([
        BotCommand(command='start',description=''),
        BotCommand(command='anketa',description=)
    ])