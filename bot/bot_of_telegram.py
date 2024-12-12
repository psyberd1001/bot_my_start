from aiogram import Dispatcher, Bot
import asyncio
from venv1.bot.handlers import start
import logging
from config import bot_token
from venv1.bot.handlers.menu import profile, about_project, test_knopka



async def main():
    bot = Bot(bot_token)
    dp = Dispatcher()
    dp.include_routers(start.router, profile.router, about_project.router, test_knopka.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

