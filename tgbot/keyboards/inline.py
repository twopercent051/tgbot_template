from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

dollar_button = InlineKeyboardButton(text='🇺🇸 Доллар США', callback_data='USD')
euro_button = InlineKeyboardButton(text='🇪🇺 Евро', callback_data='EUR')
rouble_button = InlineKeyboardButton(text='🇷🇺 Рубль', callback_data='RUB')
lira_button = InlineKeyboardButton(text='🇹🇷 Лира', callback_data='TRY')
phound_button = InlineKeyboardButton(text='🇬🇧 Фунт', callback_data='GBP')
grivna_button = InlineKeyboardButton(text='🇺🇦 Гривна', callback_data='UAH')
dram_button = InlineKeyboardButton(text='🇦🇲 Драм', callback_data='AMD')
tenge_button = InlineKeyboardButton(text='🇰🇿 Тенге', callback_data='KZT')
currency_kb = InlineKeyboardMarkup(row_width=3).add(dollar_button, euro_button, rouble_button, lira_button,\
                                       phound_button,grivna_button,dram_button, tenge_button)

reset_button = InlineKeyboardButton(text='Посчитать ещё', callback_data='reset')
reset_kb = InlineKeyboardMarkup(row_width=3).add(reset_button)

