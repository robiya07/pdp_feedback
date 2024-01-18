from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.feedback import complaint_or_suggestion
from loader import dp
from states.department_feedback import LeaveFeedback


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Assalomu alaykum. <b>PDP Academy Feedback</b> botiga xush kelibsiz!\nFeedback qoldirish uchun /feedback komandasini kiriting",
        parse_mode="HTML", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=["feedback"], state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Qaysi turdagi feedback qoldirmoqchisiz?",
        reply_markup=complaint_or_suggestion, parse_mode="HTML")
    await LeaveFeedback.first()
