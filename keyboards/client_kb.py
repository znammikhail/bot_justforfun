from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= True)  # замещает обычную клавиатуру на созданную

kb_client.row(b1, b2, b3)  #.add(b4).add(b5)

