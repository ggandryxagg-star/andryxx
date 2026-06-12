import telebot
from telebot import *


bot = telebot.TeleBot('8928265509:AAENWju3gxPclv6xOHAIcFTkLP7d_N9Qocs')


@bot.message_handler(commands=['start'])

def main(message):

    bot.send_message(message.chat.id, 'Этот бот для списаний продкутов, привета')
    
    
bot.polling(none_stop=True)