import asyncio
import logging
from aiogram import Bot, Dispatcher
from secret import TOKEN
from user_handlers import req_handler


logging.basicConfig(level=logging.INFO)
async def main() -> None:
    bot = Bot(TOKEN)
    dp = Dispatcher(bot)
    
    req_handler(dp)
    
    try:
        await dp.start_polling()
        print('ПРЫВЕТ')
    except:
        await dp.stop_polling()
        await bot.close()
        print('Bot is stopped')

if __name__ == '__main__':
    asyncio.run(main())