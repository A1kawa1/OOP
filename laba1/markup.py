from telebot import types


def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Изображение', 'Аудиофайл')
    return keyboard


def create_close():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            text='Закрыть',
            callback_data='close'
        )
    )
    return markup
