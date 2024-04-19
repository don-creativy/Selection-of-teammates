import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

bot = Bot(token="7091036049:AAGGLZHLyEUIcKqB6vCviPdxwZktAWL85Kk")

dp = Dispatcher()

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await bot.set_my_commands([
        BotCommand(command='start',description='Запуск бота'),
        BotCommand(command='help',description='справка'),
        BotCommand(Command='delete',description='Отчислиться')
    ])
    markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Привет!')]])
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='ГОВНИЩЕ', callback_data='1'),
            InlineKeyboardButton(text='переделывай', callback_data='2')],
        [
            InlineKeyboardButton(text='отчислиться', callback_data='3')]
        
    ])
    await message.answer(text="Привет", reply_markup=inline_markup)

@router.callback_query(F.data == '1')
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text='разработка')

@router.callback_query(F.data == '2')
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text='программных')

@router.callback_query(F.data == '3')
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text='модулей')

@router.callback_query()
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text=callback_query.data)

async def main():
    await dp.start_polling(bot)

dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())