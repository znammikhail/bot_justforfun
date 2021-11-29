import logging

from aiogram import Bot, Dispatcher, executor, types
from create import dp

from handlers import client,admin,other

# Configure logging
logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    print('Бот вышел в онлайн')

client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)