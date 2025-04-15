import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from src.config import conf
from src.payments.handlers import router as payment_router
from src.users.handlers import router as user_router

routers = [user_router, payment_router]
dp = Dispatcher(bot=bot)
dp.include_routers(*routers)
bot = Bot(token='7930467714:AAGnJixu-zm1bpe3MK90o4DeeALRHiTQXsM')

if __name__ == "main":
    # Включаем логирование.
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # Запускаем поток.
    try:
        asyncio.run(dp.start_polling(bot))
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
