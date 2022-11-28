# импортируем типы из библиотеки aiogram
from aiogram import types


# создаем кнопку, которая будет располагаться на клавиатуре
make_a_post_button = types.KeyboardButton('📢 Создать пост')

make_a_post_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
make_a_post_keyboard.add(make_a_post_button)
