from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reset_button = KeyboardButton('Перезапустить')

reset_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reset_kb.row(reset_button)