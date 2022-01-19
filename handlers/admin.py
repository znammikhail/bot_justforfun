from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create import bot, dp
from data_base import sqlite_db
from keyboards import admin_kb, client_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID = None

class FSMAdmin(StatesGroup):  #класс состояний
    photo = State()
    name = State()
    description = State()
    price = State()

# получаем id модератора , проверка что это админ
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)

async def make_changes(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что будем менять, Танюшка?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


# Начало диалога загрузки новой фотосессии

#@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')

# Выход из машины состояний

#@dp.message_handler(state="*", commands='отмена') # * значит все из всех состояний
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_status = await state.get_state()
        if current_status is None:
            return
        else:
            await state.finish()
            await message.reply('OK')

# Ловим первый ответ и пишем словарь

#@dp.message_handler(content_types=['photo'], state= FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  #записывавем в словарь
            data['photo'] = message.photo[0].file_id  #не файл отправляется а айди файла
        await FSMAdmin.next()
        await message.reply('Теперь введи название') #переход к следующему стэйту


# ловим второй ответ

#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  #записывавем в словарь
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')

# Ловим третий ответ

#@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  #записывавем в словарь
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи цену')

# Ловим четвертый ответ

#@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  #записывавем в словарь
            data['price'] = float(message.text)
        await sqlite_db.sql_add_command(state)
        await state.finish()

@dp.callback_query_handler(Text(startswith='del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ',''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ","")} удалена', show_alert=True)

# @dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))

@dp.message_handler(commands= 'ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=client_kb.urlkb)

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='Загрузить', state=None)
    dp.register_message_handler(cancel_handler, commands='отмена', state="*")  # * значит все из всех состояний
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state= FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(delete_item, commands=['Удалить'])


