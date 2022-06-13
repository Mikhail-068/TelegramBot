from telebot import TeleBot
from config import API_KEY, Sonya
from responses import BOT_CONFIG


bot = TeleBot(API_KEY)


@bot.message_handler()
def hi(message):
    mess = Sonya(message.text)
    bot.send_message(message.chat.id, mess)

bot.polling(none_stop=True)
