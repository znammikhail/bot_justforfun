from aiogram import types, Dispatcher
from create import bot
from keyboards import kb_client, client_kb
from data_base import sqlite_db

# @dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Привет!\nДавай начнем выбирать!", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply_to_message('Общение с ботом через лс, @ZMTestingV1bot')


# @dp.message_handler(commands=['Режим_работы'])
async def send_open(message: types.Message):
    await bot.send_message(message.from_user.id, "пн вт среда да и в любое аремя впринципе")


# @dp.message_handler(commands=['Расположение'])
async def send_place(message: types.Message):
    await bot.send_message(message.from_user.id, "спб карбышева")

# @dp.message_handler(commands=['Меню])
async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

#@dp.message_handler(commands= 'Cсылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=client_kb.urlkb)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(send_open, commands=['Режим_работы'])
    dp.register_message_handler(send_place, commands=['Расположение'])
    dp.register_message_handler(menu_command, commands=['Меню'])
    dp.register_message_handler(url_command, commands=['Ссылки'])
