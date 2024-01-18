from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

complaint_or_suggestion = InlineKeyboardMarkup()
complaint_or_suggestion.insert(InlineKeyboardButton('✅ Taklif', callback_data='feed_✅ Taklif'))
complaint_or_suggestion.insert(InlineKeyboardButton('❌ Shikoyat', callback_data='feed_❌ Shikoyat'))
