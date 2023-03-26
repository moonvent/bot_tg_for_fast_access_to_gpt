from telebot.types import Message
from bot.markups.main_menu import markup_main_menu

from bot.util import bot, get_message_info, schedule_message, send_message
from services.bot.filters_for_messages import start_conversation_message_filter
from services.constants.commands import START_COMMANDS
from services.constants.texts import I_THINK_TEXT, INPUT_QUESTION_TEXT, MAIN_MENU_TEXT
from services.database.models.conversations import get_current_conversation
from services.openai.util import send_question


# @bot.message_handler(func=start_conversation_message_filter)
@bot.message_handler(func=start_conversation_message_filter)
def command_start_conversation(message: Message):
    message_info = get_message_info(message=message)
    schedule_message(chat_id=message_info.chat_id,
                     text=INPUT_QUESTION_TEXT,
                     reply_markup=markup_main_menu(),
                     method=get_next_question)

    
def get_next_question(message: Message):
    message_info = get_message_info(message=message)
    send_message(chat_id=message_info.chat_id,
                 text=I_THINK_TEXT)
    text = send_question(user_id=message_info.chat_id,
                         text=message_info.text,
                         conversation_id=get_current_conversation(user_id=message_info.chat_id))
    schedule_message(chat_id=message_info.chat_id,
                     text=text,
                     method=get_next_question)

