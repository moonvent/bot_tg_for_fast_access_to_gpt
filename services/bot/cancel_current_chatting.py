from services.constants.buttons import CONTINUE_EXIST_BUTTON, START_NEW_CONVERSATION_BUTTON
from services.constants.commands import START_COMMANDS, CHECK_CONVERSATION_COMMANDS 


def check_on_reset_word(text: str) -> bool:
    return text in (*START_COMMANDS,
                    START_NEW_CONVERSATION_BUTTON,
                    *CHECK_CONVERSATION_COMMANDS ,
                    CONTINUE_EXIST_BUTTON)
