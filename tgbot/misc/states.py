from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMCurrency(StatesGroup):
    first_cur = State()
    summ = State()
    second_cur = State()