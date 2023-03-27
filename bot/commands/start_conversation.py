from threading import Thread
from telebot.types import Message
from bot.markups.main_menu import markup_main_menu
from bot.markups.to_main_menu import markup_to_main_menu

from bot.util import MessageInfo, bot, get_message_info, schedule_message, send_message
from services.bot.cancel_current_chatting import check_on_reset_word
from services.bot.commands.start_conversation import prepare_text_to_output_in_tg
from services.bot.filters_for_messages import start_conversation_message_filter
from services.constants.commands import START_COMMANDS
from services.constants.texts import I_THINK_TEXT, INPUT_QUESTION_TEXT, MAIN_MENU_TEXT, WAIT_FOR_NEXT_QUESTION
from services.database.models.conversations import get_current_conversation
from services.database.models.sessions import reset_current_conversation
from services.openai.util import send_question


@bot.message_handler(func=start_conversation_message_filter)
def command_start_conversation(message: Message):
    message_info = get_message_info(message=message)

    reset_current_conversation(user_id=message_info.chat_id)

    schedule_message(chat_id=message_info.chat_id,
                     text=INPUT_QUESTION_TEXT,
                     method=get_next_question,
                     reply_markup=markup_to_main_menu())

    
def get_next_question(message: Message):
    message_info = get_message_info(message=message)

    if check_on_reset_word(text=message_info.text):
        # if user press other button
        bot.process_new_messages([message])
        return

    send_message(chat_id=message_info.chat_id,
                 text=I_THINK_TEXT)

    Thread(target=send_ai_response, 
           args=(message_info,),
           daemon=True).start()


def send_ai_response(message_info: MessageInfo):
    text = send_question(user_id=message_info.chat_id,
                         text=message_info.text,
                         conversation_id=get_current_conversation(user_id=message_info.chat_id))
    text = prepare_text_to_output_in_tg(text=text)
    schedule_message(chat_id=message_info.chat_id,
                     text=text,
                     method=get_next_question,
                     reply_markup=markup_main_menu())
    send_message(chat_id=message_info.chat_id,
                 text=WAIT_FOR_NEXT_QUESTION)


