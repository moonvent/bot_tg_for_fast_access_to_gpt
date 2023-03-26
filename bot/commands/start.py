from telebot.types import Message
from bot.markups.main_menu import markup_main_menu

from bot.util import bot, get_message_info, send_message
from services.constants.commands import START_COMMANDS
from services.constants.texts import MAIN_MENU_TEXT
from services.database.models.sessions import create_user_session


@bot.message_handler(commands=START_COMMANDS)
def command_start(message: Message):
    chat_id = get_message_info(message=message).chat_id
    start(chat_id=chat_id)
    
    
def start(chat_id: int):
    create_user_session(user_id=chat_id)

    send_message(chat_id=chat_id,
                 text=MAIN_MENU_TEXT,
                 reply_markup=markup_main_menu())

