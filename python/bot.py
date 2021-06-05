import telebot

import bot_setup
from bot_handler import Handler
from time import sleep
import sys

bot = telebot.TeleBot(bot_setup.TOKEN, parse_mode=None)
handler = Handler(bot)
flag = True

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    handler.send_welcome(message)

@bot.message_handler(commands=['loop'])
def loop(msg):
    while flag:
        bot.send_message(msg.chat.id, "ping")
        sleep(1)

@bot.message_handler(commands=['stop'])
def stop(message):
    global flag
    if message.from_user.id == bot_setup.ADMIN_ID:
        flag = False
        bot.send_message(message.chat.id, "stopped")
        os._exit()
    else:
        bot.send_message(message.from_user.id, 'Выключить может только админ', reply_markup=handler.create_markup(2, ['5from 6 to 8', '-A1from16', '3123 from 4 to8', '0']))


@bot.message_handler(func=lambda message: True)
def get_text_message(message):
    handler.get_text_messages(message)

bot.polling()
