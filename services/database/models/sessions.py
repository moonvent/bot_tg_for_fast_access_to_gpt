from services.constants.session_flags import CURRENT_CONVERSATION_ID
from services.database.db_models import Sessions


def add_current_conversation_to_session(user_id: int,
                                        conversation_id: int):
    session = Sessions.get(Sessions.user_id == user_id)
    session.data[CURRENT_CONVERSATION_ID] = conversation_id
    session.save()


def create_user_session(user_id: int):
    if not Sessions.filter(Sessions.user_id == user_id):
        Sessions(user_id=user_id).save()

