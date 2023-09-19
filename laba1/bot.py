import telebot
import requests
from dotenv import load_dotenv
from random import choice
import os

from markup import create_keyboard, create_close


load_dotenv()
TOKEN_TG = os.getenv('TOKEN_TG')
bot = telebot.TeleBot(token=TOKEN_TG)

TASK_TEXT = ('Написать на Python бота для Телеграм\n'
             'Функциональные требования к боту:\n'
             'Работа с изображениями (выслать сгенерированное или готовое по запросу)\n'
             'Работа с аудиофайлами (выслать сгенерированный или готовый по запросу)\n'
             'Реализовать команду для получения ссылки на публичный репозиторий с исходниками подготовленного бота\n'
             'Оформить одну часть команд кнопками, другую -текстом.'
             )
GIT_URL = os.getenv('GIT_URL')


class GetImageAudio():
    api_image = 'https://api.thecatapi.com/v1/images/search'

    @classmethod
    def get_image(cls):
        return requests.get(cls.api_image).json()[0].get('url')

    @classmethod
    def get_audio(cls):
        cur_dir = os.getcwd()

        audios = os.listdir(os.path.join(cur_dir, 'audio'))
        if not audios:
            return None

        return os.path.join(cur_dir, 'audio', choice(audios))


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=TASK_TEXT,
        reply_markup=create_keyboard()
    )


@bot.message_handler(commands=['keyboard'])
def start(message: telebot.types.Message):
    bot.send_message(
        chat_id=message.from_user.id,
        text='Добавление клавиатуры',
        reply_markup=create_keyboard()
    )


@bot.message_handler(commands=['git_url'])
def start(message: telebot.types.Message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=f'<b><a href="{GIT_URL}">Ссылка на git</a></b>',
        reply_markup=create_close(),
        parse_mode='HTML'
    )


@bot.message_handler(content_types=['text'])
def image_audio(message: telebot.types.Message):
    chat_id = message.from_user.id

    if message.text == 'Изображение':
        bot.send_photo(
            chat_id=chat_id,
            photo=GetImageAudio.get_image(),
            caption='вот кот',
            reply_markup=create_close()
        )
    elif message.text == 'Аудиофайл':
        audio = GetImageAudio.get_audio()
        print(audio)
        if audio is None:
            bot.send_message(
                chat_id=chat_id,
                text='Аудиофайлы отстутствуют',
                reply_markup=create_close()
            )
            return
        audio = open(audio, 'rb')
        bot.send_audio(
            chat_id=chat_id,
            audio=audio,
            caption='вот музыка',
            reply_markup=create_close(),
            timeout=60
        )
        audio.close()


@bot.callback_query_handler(func=lambda _: True)
def query_handler_bot_main(call: telebot.types.CallbackQuery):
    chat_id = call.message.chat.id
    if call.data == 'close':
        bot.delete_message(
            chat_id=chat_id,
            message_id=call.message.message_id
        )
        bot.clear_step_handler_by_chat_id(chat_id=chat_id)


if __name__ == '__main__':
    bot.infinity_polling(timeout=600)
