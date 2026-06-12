import telebot
from telebot import *


bot = telebot.TeleBot('8928265509:AAFxL2vRWzFV5zIqwuGznTYXejt0ne7CmiU')


@bot.message_handler(commands=['start'])

def start(message):

    bot.send_message(message.chat.id, 'Этот бот для списаний продкутов, привета')
    
    bot.register_next_step_handler(spisi)

def spisi(message):

    pass





bot.polling(none_stop=True)