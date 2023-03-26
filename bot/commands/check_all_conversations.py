from telebot.types import Message
from bot.markups.all_conversations import markup_all_conversations
from bot.util import bot
from bot.util import get_message_info, send_message
from services.bot.filters_for_messages import check_conversations_message_filter
from services.constants.texts import ALL_YOUR_CONVERSATIONS
from services.database.models.sessions import reset_current_conversation


@bot.message_handler(func=check_conversations_message_filter)
def check_conversations(message: Message):
    message_info = get_message_info(message=message)

    reset_current_conversation(user_id=message_info.chat_id)

    send_message(chat_id=message_info.chat_id,
                 text=ALL_YOUR_CONVERSATIONS,
                 reply_markup=markup_all_conversations(user_id=message_info.chat_id))

