import telebot

# Токен вашего бота (замените на свой)
BOT_TOKEN = "8928265509:AAENWju3gxPclv6xOHAIcFTkLP7d_N9Qocs"

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    response = f"Привет, {user_name}! Я простой Telegram‑бот на библиотеке Telebot."
    bot.reply_to(message, response)

# Обранотчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
Доступные команды:
/start — Начать работу с ботом
/help — Показать эту справку
/echo <текст> — Повторить ваш текст
/info — Информация о боте
    """
    bot.send_message(message.chat.id, help_text)

# Обработчик команды /echo
@bot.message_handler(commands=['echo'])
def echo_command(message):
    # Извлекаем текст после команды
    text_to_echo = ' '.join(message.text.split()[1:])
    if text_to_echo:
        bot.reply_to(message, f"Эхо: {text_to_echo}")
    else:
        bot.reply_to(message, "Напишите текст после команды /echo")

# Обработчик команды /info
@bot.message_handler(commands=['info'])
def send_info(message):
    info_text = "Этот бот создан как базовый шаблон на библиотеке pyTelegramBotAPI."
    bot.send_message(message.chat.id, info_text)

# Обработчик текстовых сообщений (не команд)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = f"Вы сказали: {message.text}\nИспользуйте /help для списка команд."
    bot.reply_to(message, response)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
