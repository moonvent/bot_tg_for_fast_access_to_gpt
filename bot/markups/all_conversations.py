from telebot.types import CallbackQuery
from bot.commands.start_conversation import get_next_question
from bot.markups.to_main_menu import markup_to_main_menu
from services.bot.markups.all_conversations import prepare_to_markup_user_conversations
from bot.util import bot, get_message_info, schedule_message
from services.constants.buttons import SELECT_CONVERSATION
from services.constants.texts import INPUT_QUESTION_TEXT
from services.database.models.sessions import set_current_conversation


def markup_all_conversations(user_id: int):
    markup = markup_to_main_menu(row_width=1)
    
    conversations_buttons = prepare_to_markup_user_conversations(user_id=user_id)
    markup.add(*conversations_buttons)
    return markup


def __check_conversation_callback(callback: CallbackQuery) -> bool:
    try:
        return callback.data.split('_')[0] == SELECT_CONVERSATION[:-3]
    except:
        return False


@bot.callback_query_handler(func=__check_conversation_callback)
def change_current_conversation(callback: CallbackQuery):
    # delete_message(message_id=callback.message.id,
    #                chat_id=callback.from_user.id)
    message_info = get_message_info(message=callback,
                                    callback_str=SELECT_CONVERSATION)
    chat_id = callback.from_user.id

    set_current_conversation(user_id=chat_id,
                             conversation_id_in_db=int(message_info.text))

    schedule_message(chat_id=message_info.chat_id,
                     text=INPUT_QUESTION_TEXT,
                     method=get_next_question,
                     reply_markup=markup_to_main_menu())

