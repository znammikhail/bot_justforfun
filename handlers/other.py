import string
import mat
from create import dp
from aiogram import types, Dispatcher

# @dp.message_handler()
async def echo(message: types.Message):
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}.intersection(set(mat.ar)) != set():
        await message.reply('Маты запрещены')
        await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo)