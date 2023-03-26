from telebot.types import InlineKeyboardButton
from services.config import CONVERSATION_TITLE_FOR_BUTTONS_LEN
from services.constants.buttons import SELECT_CONVERSATION
from services.constants.markups import INLINE_MARKUP_STURCTURE
from services.database.models.conversations import get_all_user_conversations


def prepare_to_markup_user_conversations(user_id: int) -> INLINE_MARKUP_STURCTURE:
    result = []

    for conversation in get_all_user_conversations(user_id=user_id):
        title = conversation.title

        result.append(InlineKeyboardButton(text=title[:CONVERSATION_TITLE_FOR_BUTTONS_LEN] if len(title) > CONVERSATION_TITLE_FOR_BUTTONS_LEN else title,
                                           callback_data=SELECT_CONVERSATION.format(conversation.id)
                                           )
                      )

    return result
