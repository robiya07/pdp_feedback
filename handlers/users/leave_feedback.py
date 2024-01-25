from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from loader import dp, bot
from states.department_feedback import LeaveFeedback


@dp.callback_query_handler(lambda query: query.data.startswith("feed"), state=LeaveFeedback.feedback)
async def feedback_callback(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    msg = ""
    if "✅" in query.data:
        msg = f"Taklifingizni tekst ko'rinishida kiriting"
        await state.update_data(feedback="taklif")
    elif "❌" in query.data:
        msg = "Shikoyatingizni tekst ko'rinishida kiriting"
        await state.update_data(feedback="shikoyat")
    await query.message.edit_text(msg, parse_mode="HTML")
    await LeaveFeedback.next()


@dp.message_handler(state=LeaveFeedback.description)
async def feedback_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    feedback = data["feedback"]
    "<b>Taklifingiz uchun Rahmat!!!</b>Taklifingiz sir saqlangan holda "
    if feedback == "taklif":
        msg = f"<b>Taklifingiz uchun Rahmat!</b>\n\nTaklifingiz sir saqlangan holda <b>PDP Academy</b> jamoasiga yetkazildi va tez orada ko'rib chiqiladi.\nYana taklifingiz bo'lsa /feedback komandasini kiriting"
        admin_msg = f"<b>✅ Taklif:</b>\n{message.text}"
    else:
        msg = f"<b>Shikoyatingiz uchun Rahmat!</b>\n\nShikoyatingiz sir saqlangan holda <b>PDP Academy</b> jamoasiga yetkazildi va tez orada ko'rib chiqiladi.\nYana shikoyatingizjusdd bo'lsa /feedback komandasini kiriting"
        admin_msg = f"<b>❌ Shikoyat</b>\n{message.text}"
    await message.answer(msg, parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
    for department in ADMINS:
        try:
            await bot.send_message(department, admin_msg, parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
        except Exception:
            pass
