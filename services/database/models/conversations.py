from typing import Optional
from services.config import CONVERSATION_TITLE_LEN
from services.constants.session_flags import CURRENT_CONVERSATION_ID
from services.database.db_models import Conversations, Sessions


def create_conversation(user_id: int,
                        title: str,
                        conversation_id: str):
    Conversations(user_id=user_id, 
                  title=title[:CONVERSATION_TITLE_LEN],
                  conversation_id=conversation_id).save()


def get_current_conversation(user_id: int) -> Optional[str]:
    return (Sessions
            .get(Sessions.user_id == user_id)
            .data
            .get(CURRENT_CONVERSATION_ID))


def get_previous_conversation_body(conversation_id: str) -> list:
    if conversation := Conversations.filter(Conversations.conversation_id == conversation_id).first():
        return conversation.body['chat']

    else:
        return []


def add_to_body_new_response(conversation_id: str,
                             body: list):
    conversation = Conversations.get(Conversations.conversation_id == conversation_id)
    conversation.body['chat'] = body
    conversation.save()


def get_all_user_conversations(user_id: int) -> tuple[Conversations]:
    return Conversations.filter(Conversations.user_id == user_id).order_by(Conversations.id.desc())


def get_conversation_openai_id(conversation_id_in_db: int) -> str:
    return Conversations.get(Conversations.id == conversation_id_in_db).conversation_id


