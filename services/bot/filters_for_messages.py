from functools import partial
from typing import Iterable
from telebot.types import Message

from services.constants.filters import CHECK_CONVERSATIONS_FILTER_TEXT, START_CONVERSATION_FILTER_TEXT


def __filter_message_to_handler(message_text: str,
                                need_text: Iterable[str]) -> bool:
    return message_text in need_text


def start_conversation_message_filter(message: Message) -> bool:
    return __filter_message_to_handler(message_text=message.text, 
                                       need_text=START_CONVERSATION_FILTER_TEXT)


def check_conversations_message_filter(message: Message) -> bool:
    return __filter_message_to_handler(message_text=message.text, 
                                       need_text=CHECK_CONVERSATIONS_FILTER_TEXT)
