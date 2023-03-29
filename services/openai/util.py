import os
import openai

from services.config import OPEN_AI_MODEL
from services.constants.texts import ERROR_IN_ANSWER_GENERATION
from services.database.models.conversations import add_to_body_new_response, create_conversation, get_previous_conversation_body
from services.database.models.sessions import add_current_conversation_to_session
from services.logs import log


openai.api_key = os.environ['OPENAI_TOKEN']


def send_question(text: str,
                  user_id: int,
                  conversation_id: str = None) -> str:

    previous_body = get_previous_conversation_body(conversation_id=conversation_id)

    new_body = previous_body + [{"role": "user", "content": text}]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=new_body,
        )
    except Exception as e:
        log.exception("Error in answer generation")
        return ERROR_IN_ANSWER_GENERATION

    else:
        if not conversation_id:
            conversation_id = response.id
            create_conversation(user_id=user_id,
                                title=text,
                                conversation_id=conversation_id)
            add_current_conversation_to_session(user_id=user_id,
                                                conversation_id=conversation_id)

        add_to_body_new_response(conversation_id=conversation_id,
                                 body=new_body + [{'role': response.choices[0].message.role,
                                                   'content': response.choices[0].message.content}])

        return response.choices[0].message.content 
