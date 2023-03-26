"""
    Markups patterns

    ReplyMarkups: it's usually a tuple with tuples, where element is button text, 
        structure of this: Tuple[Tuple[str, ...]] or 
"""


from typing import Literal, Tuple
from services.constants.buttons import CONTINUE_EXIST_BUTTON, START_NEW_CONVERSATION_BUTTON


REPLY_MARKUP_STURCTURE = Tuple[Tuple[str, ...]]


MARKUP_MAIN_MENU = ((START_NEW_CONVERSATION_BUTTON, CONTINUE_EXIST_BUTTON), 
                    ())

