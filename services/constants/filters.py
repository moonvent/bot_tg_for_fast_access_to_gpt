
from typing import Iterable
from services.constants.buttons import START_NEW_CONVERSATION_BUTTON

from services.constants.commands import START_CONVERSATION_COMMANDS


def __decorate_commands(commands: Iterable[str]) -> list:
    return ['/' + command for command in commands]


START_CONVERSATION_FILTER_TEXT = __decorate_commands(START_CONVERSATION_COMMANDS) + [START_NEW_CONVERSATION_BUTTON]

