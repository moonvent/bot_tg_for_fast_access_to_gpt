
from typing import Iterable
from services.constants.buttons import CONTINUE_EXIST_BUTTON, START_NEW_CONVERSATION_BUTTON

from services.constants.commands import CHECK_CONVERSATION_COMMANDS, START_CONVERSATION_COMMANDS


def decorate_commands(commands: Iterable[str]) -> list:
    return ['/' + command for command in commands]


START_CONVERSATION_FILTER_TEXT = decorate_commands(START_CONVERSATION_COMMANDS) + [START_NEW_CONVERSATION_BUTTON]

CHECK_CONVERSATIONS_FILTER_TEXT = decorate_commands(CHECK_CONVERSATION_COMMANDS) + [CONTINUE_EXIST_BUTTON]

