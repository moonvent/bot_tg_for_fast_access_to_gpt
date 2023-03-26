from services.constants.session_flags import CURRENT_CONVERSATION_ID
from services.database.db_models import Sessions
from services.database.models.conversations import get_conversation_openai_id


def add_current_conversation_to_session(user_id: int,
                                        conversation_id: int):
    session = Sessions.get(Sessions.user_id == user_id)
    session.data[CURRENT_CONVERSATION_ID] = conversation_id
    session.save()


def create_user_session(user_id: int):
    if not Sessions.filter(Sessions.user_id == user_id):
        Sessions(user_id=user_id).save()


def reset_current_conversation(user_id: int):
    session = Sessions.get(Sessions.user_id == user_id)
    session.data[CURRENT_CONVERSATION_ID] = None
    session.save()


def set_current_conversation(user_id: int,
                             conversation_id_in_db: int):
    session = Sessions.get(Sessions.user_id == user_id)
    session.data[CURRENT_CONVERSATION_ID] = get_conversation_openai_id(conversation_id_in_db)
    session.save()

