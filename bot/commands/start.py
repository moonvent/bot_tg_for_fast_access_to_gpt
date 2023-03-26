from telebot.types import Message
from bot.markups.main_menu import markup_main_menu

from bot.util import bot, get_message_info, send_message
from services.constants.commands import START_COMMANDS
from services.constants.texts import MAIN_MENU_TEXT


@bot.message_handler(commands=START_COMMANDS)
def command_start(message: Message):
    message_info = get_message_info(message=message)
    send_message(chat_id=message_info.chat_id,
                 text=MAIN_MENU_TEXT,
                 reply_markup=markup_main_menu())

    

