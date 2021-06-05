#pip3 install PyTelegramBotAPI
import numexpr as ne
from telebot import types
from convert import *

import bot_setup

class Handler:
    def __init__(self, bot):
        self.bot = bot

    def send_welcome(self, message):
        print(message.json)
        self.bot.reply_to(message, f'Я бот, который переводит одно число в другую систему счисления.\nПример: 5 from 8 to 4\nЭто из 5 в восьмеричной системе в четверичную.')

    def get_text_messages(self, message):
        self.last_message = message

        text_message = message.json['text']
        # обработчик
        try:
            text_answer = convert_from_text(text_message)
        except:
            text_answer = 'Некорректное выражение. Попробуйте ввести пример заново.'

        print(f'|bot|: {text_answer}')
        self.bot.send_message(message.from_user.id, text_answer, reply_markup=self.create_markup(2, ['5from 6 to 8', '-A1from16', '3123 from 4 to8', '0']))

    def create_markup(self, row_width, items = []):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        btn = []
        for item in items:
            btn = types.KeyboardButton(item)
            btn2 = types.KeyboardButton(item)
            markup.add(btn, btn2)

        return markup

    def get_name(self, message):
        last_name = ''
        first_name = ''
        try:
            last_name = message.from_user.last_name
        except:
            pass
        try:
            first_name = message.from_user.first_name
        except:
            pass
        return f'{last_name} {first_name}'

    def run_bot(self):
            self.bot.send_message(bot_setup.ADMIN_ID, 'Бот Pem_Test_bot был запущен')
            self.bot.polling(none_stop=True) # потом удалить
            last_message = f'Bye! User {self.get_name(self.last_message)} killed me.'
            print(last_message)
            self.bot.send_message(bot_setup.ADMIN_ID, last_message)
            #exit()
            '''
        try:
            self.bot.polling(none_stop=True)
        except:
            last_message = f'Bye! User {self.get_name(self.last_message)} kill me :('
            print(last_message)
            self.bot.send_message(bot_setup.ADMIN_ID, last_message)
            exit()
        '''

if __name__ == '__main__':
        a = ''
        ne.evaluate('5555**55555')
        print(str())
