import asyncio

from aiogram import Bot, Dispatcher
from handlers import include_routers

bot = Bot(token="7091036049:AAGGLZHLyEUIcKqB6vCviPdxwZktAWL85Kk")
dp = Dispatcher()

async def main():
    '''21'''
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())