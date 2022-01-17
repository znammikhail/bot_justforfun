from aiogram import Bot, types
from data_base import sqlite_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text

async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()   # подключаемся к базе даннных или создаем ее

bot = Bot(token= '643068252:AAEvu6D8Y1L_UjuTKBdULkKuqg335EZopJo')
dp = Dispatcher(bot)

answ = dict()

# inline кнопки
urlkb = InlineKeyboardMarkup(row_width=1)  # ширина ряда
urlButton1 = InlineKeyboardButton(text='ссылка на таню', url='https://www.instagram.com/tanyyep/?hl=ru')
urlButton2 = InlineKeyboardButton(text='ссылка на мишу', url='https://www.instagram.com/znamenskymihail/?hl=ru')
urlkb.add(urlButton1, urlButton2)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='за', callback_data='like_1'), InlineKeyboardButton(text='против', callback_data='like_-1'))

@dp.message_handler(commands= 'ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

@dp.message_handler(commands= 'test')
async def url_command(message: types.Message):
    await message.answer('инлайн кнопки', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback:  types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    print(res)
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)
    # await callback.message.answer('Вы проголосовали')  # соотвественно в личку
    # await callback.answer('Это сообщение сейчас исчезнет')  # даем понять что нужный код исполнен. можно пустую строку

executor.start_polling(dp, skip_updates=True)