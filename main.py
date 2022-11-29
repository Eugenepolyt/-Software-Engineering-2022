import telebot
from telebot import types
from FilmFinder import FilmFinder
from RandomFilm import RandomFilm
from RequestManager import RequestManager
from Translator import Translator

bot = telebot.TeleBot('5807556514:AAHc29-KzxDIn7J4Vozn0utcdS58WXGLfD4')

welcome_message = open('WelcomeMessage.txt', 'r', encoding="utf-8").read()
request_manager = RequestManager()
translator = Translator()
film_finder = FilmFinder(request_manager, translator)

markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton("Случайный фильм", callback_data="random"))
markup.add(types.InlineKeyboardButton("Найти фильм", callback_data="search"))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, welcome_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_film_from_user(message):
    bot.send_message(message.chat.id, film_finder.get_film_characteristics(message.text), parse_mode="html")
    bot.send_message(message.chat.id, 'Что будем смотреть дальше?🤔', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "search":
        bot.send_message(call.message.chat.id, "Введите название фильма на любом языке", parse_mode="html")
    bot.answer_callback_query(call.id)


bot.infinity_polling()
