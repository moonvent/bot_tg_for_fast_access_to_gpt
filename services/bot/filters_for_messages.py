from functools import partial
from typing import Iterable
from telebot.types import Message
from services.constants.buttons import START_NEW_CONVERSATION_BUTTON

from services.constants.commands import START_CONVERSATION_COMMANDS


def __filter_message_to_handler(message_text: str,
                                need_text: Iterable[str]) -> bool:
    return message_text in need_text


def __decorate_commands(commands: Iterable[str]) -> list:
    return ['/' + command for command in commands]


def start_conversation_message_filter(message: Message) -> bool:
    return __filter_message_to_handler(message_text=message.text, 
                                       need_text=__decorate_commands(START_CONVERSATION_COMMANDS) + [START_NEW_CONVERSATION_BUTTON])

