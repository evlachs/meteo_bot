# импортируем типы из библиотеки aiogram
from aiogram import types

# создаем все кнопки, которые буду располагаться на клавиатурах
sale_button = types.KeyboardButton('Продажа 💲')
purchase_button = types.KeyboardButton('Покупка 🛒')
advertisement_button = types.KeyboardButton('Реклама 📺')
question_button = types.KeyboardButton('Вопрос ❓')
cancel_button = types.InlineKeyboardButton('Отмена❌', callback_data='cancel')
cancel_photo_button = types.InlineKeyboardButton('Объявление без фото❌', callback_data='cancel_photo')
confirm_post_button = types.InlineKeyboardButton('Сформировать пост✔️', callback_data='confirm_post')
finish_photo_button = types.InlineKeyboardButton('Завершить добавление', callback_data='finish_photo')


# по очереди создаем все необходимые клавиатуры, после чего добавляем в них кнопки
choose_a_post_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
choose_a_post_keyboard.add(sale_button, purchase_button).add(advertisement_button, question_button)

cancel_photo_keyboard = types.InlineKeyboardMarkup()
cancel_photo_keyboard.add(cancel_photo_button)

confirm_post_keyboard = types.InlineKeyboardMarkup()
confirm_post_keyboard.add(confirm_post_button).add(cancel_button)

photo_keyboard = types.InlineKeyboardMarkup()
photo_keyboard.add(finish_photo_button)
