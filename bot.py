import telebot
import config


class Bot:

    def __init__(self):
        self.token = config.bot_token
        self.chat_id = config.chat_id
        self.bot = telebot.TeleBot(self.token)

    def send_message(self, message):
        self.bot.send_message(config.chat_id, message, parse_mode='html')
