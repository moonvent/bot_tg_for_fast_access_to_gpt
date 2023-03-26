"""
    Markups patterns

    ReplyMarkups: it's usually a tuple with tuples, where element is button text, 
        structure of this: Tuple[Tuple[str, ...]] or 
"""


from typing import Literal, Tuple
from services.constants.buttons import CONTINUE_EXIST_BUTTON, START_NEW_CONVERSATION_BUTTON, TO_MAIN_MENU_BUTTON, TO_MAIN_MENU_CALLBACK


BUTTON_TITLE = str
BUTTON_CALLBACK = str

ROW_BUTTONS = Tuple[BUTTON_TITLE, ...]

INLINE_BUTTON = Tuple[BUTTON_TITLE, BUTTON_CALLBACK]
ROW_INLINE_BUTTONS = Tuple[INLINE_BUTTON, ...]

REPLY_MARKUP_STURCTURE = Tuple[ROW_BUTTONS, ...]
INLINE_MARKUP_STURCTURE = Tuple[ROW_INLINE_BUTTONS, ...]


MARKUP_MAIN_MENU = ((START_NEW_CONVERSATION_BUTTON, CONTINUE_EXIST_BUTTON), 
                    ())


INLINE_MARKUP_TO_MAIN_MENU = (((TO_MAIN_MENU_BUTTON, TO_MAIN_MENU_CALLBACK), ),)
