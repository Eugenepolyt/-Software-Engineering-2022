import telebot
from telebot import types
from FilmFinder import FilmFinder
from RequestManager import RequestManager
from Translator import Translator

bot = telebot.TeleBot('5807556514:AAHc29-KzxDIn7J4Vozn0utcdS58WXGLfD4')

welcome_message = open('WelcomeMessage.txt', 'r', encoding="utf-8").read()
request_manager = RequestManager()
translator = Translator()
film_finder = FilmFinder(request_manager, translator)

markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton("Найти фильм", callback_data="search"))
arrayOfActiveUsers = []

useless_content_types = ["audio", "document", "photo", "sticker",
                         "video", "video_note", "voice", "location", "contact",
                         "new_chat_mebers", "left_chat_member", "new_chat_title",
                         "new_chat_photo", "delete_chat_photo", "group_chat_created",
                         "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                         "migrate_from_chat_id", "pinned_message"]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, welcome_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=useless_content_types)
def get_error_message(message):
    err_msg = 'Я не знаю, что на это ответить 🤯\n\n Выберите нужную опцию👇'
    bot.send_message(message.chat.id, err_msg, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_film_from_user(message):
    if message.chat.id in arrayOfActiveUsers:
        bot.send_message(message.chat.id, film_finder.get_film_characteristics(message.text), parse_mode="html")
        arrayOfActiveUsers.remove(message.chat.id)
        bot.send_message(message.chat.id, 'Что будем смотреть дальше?🤔', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста выберите нужную опцию👇', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "search":
        bot.send_message(call.message.chat.id, "Введите название фильма на любом языке", parse_mode="html")
        arrayOfActiveUsers.append(call.message.chat.id)
    bot.answer_callback_query(call.id)


bot.infinity_polling()
