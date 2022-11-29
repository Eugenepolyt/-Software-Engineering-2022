import telebot
from telebot import types

bot = telebot.TeleBot('5807556514:AAHc29-KzxDIn7J4Vozn0utcdS58WXGLfD4')

welcome_message = open('WelcomeMessage.txt', 'r', encoding="utf-8").read()

markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton("Найти фильм", callback_data="search"))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, welcome_message, parse_mode='html', reply_markup=markup)


bot.infinity_polling()
