import telegram
import os

from dotenv import load_dotenv
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup


load_dotenv()


TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


def roll_it(update, context):
    chat = update.effective_chat
    text = (
        'Сколько костей нужно бросить? Напишите в формате "2к6" или "2d10".'
    )
    buttons = ReplyKeyboardMarkup(
        [['к4', 'к6', 'к8', 'к10', 'к12', 'к20']],
        resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text=text,
        reply_markup=buttons
    )


def main():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    updater = Updater(token=TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('roll', roll_it))
