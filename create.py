from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Initialize bot and dispatcher
storage = MemoryStorage()

bot = Bot(token='2140173049:AAFjBhpHQMdM0eT84VPTmOaC91nsGU--1rE')
dp = Dispatcher(bot, storage=storage)

