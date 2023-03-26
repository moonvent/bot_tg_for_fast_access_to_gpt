from telebot.types import Message
from bot.markups.main_menu import markup_main_menu

from bot.util import bot, get_message_info, send_message
from services.bot.filters_for_messages import start_conversation_message_filter
from services.constants.commands import START_COMMANDS
from services.constants.texts import MAIN_MENU_TEXT


# @bot.message_handler(func=start_conversation_message_filter)
@bot.message_handler(func=start_conversation_message_filter)
def command_start_conversation(message: Message):
    message_info = get_message_info(message=message)
    send_message(chat_id=message_info.chat_id,
                 text='sex',
                 reply_markup=markup_main_menu())

    

