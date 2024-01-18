from aiogram.dispatcher.filters.state import StatesGroup, State


class LeaveFeedback(StatesGroup):
    feedback = State()
    description = State()
