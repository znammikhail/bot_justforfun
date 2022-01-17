from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Примеры_фотоссесий')
b4 = KeyboardButton('/Ссылки')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard= True)  # замещает обычную клавиатуру на созданную
kb_client.add(b1).add(b2).add(b3).add(b4)  #.add(b4).add(b5)

urlkb = InlineKeyboardMarkup(row_width=1)  # ширина ряда
urlButton1 = InlineKeyboardButton(text='ссылка на таню', url='https://www.instagram.com/tanyyep/?hl=ru')
urlButton2 = InlineKeyboardButton(text='ссылка на мишу', url='https://www.instagram.com/znamenskymihail/?hl=ru')

urlkb.add(urlButton1, urlButton2)
