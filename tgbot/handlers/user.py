from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold

from tgbot.keyboards.inline import currency_kb
from tgbot.keyboards.reply import reset_kb
from tgbot.misc.states import FSMCurrency
from tgbot.misc.request import get_currency



parameters = []
async def user_start(message: Message):
    await message.answer("Приветствую\nТут можно быстро посчитать конвертацию в популярных валютах")
    await FSMCurrency.first_cur.set()
    await message.answer("Выберите валюту, которую будете менять", reply_markup=currency_kb)

async def first_currency_reg(callback: CallbackQuery):
    global first_currency
    first_currency = callback.data
    parameters.append(first_currency)
    await FSMCurrency.next()
    await callback.message.answer('Теперь введите сумму')


async def summ_reg(message: Message):
    num = message.text.replace(',', '.')
    try:
        global summ
        summ = float(num)
        parameters.append(summ)
        await FSMCurrency.next()
        await message.answer('Введите вторую валюту', reply_markup=currency_kb)
    except:
        await message.answer('Вы ввели не число, введите еще раз')
        await message.answer(num)
        await FSMCurrency.summ.set()


async def second_currency_reg(callback: CallbackQuery):
    second_currency = callback.data
    parameters.append(second_currency)
    await callback.message.answer('Получаем результат. Подождите...')
    result = await get_currency(first_currency, second_currency, summ)
    text = [
        f'{hbold("Поменяли")} {summ} {first_currency}.',
        f'{hbold("Получилось")} {result} {second_currency}'
    ]
    await callback.message.answer(text='\n'.join(text), reply_markup=reset_kb)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state='*')
    dp.register_message_handler(user_start, lambda c: c.text == 'Перезапустить', state='*')
    dp.register_callback_query_handler(first_currency_reg, state=FSMCurrency.first_cur)
    dp.register_message_handler(summ_reg, state=FSMCurrency.summ)
    dp.register_callback_query_handler(second_currency_reg, state=FSMCurrency.second_cur)

