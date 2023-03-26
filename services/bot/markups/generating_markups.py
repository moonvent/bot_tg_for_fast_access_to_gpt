from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from services.constants.markups import REPLY_MARKUP_STURCTURE


def reply_markup(markup_pattern: REPLY_MARKUP_STURCTURE,
                 resize_keyboard: bool = True,
                 one_time_keyboard: bool = False,
                 input_field_placegolder: str = '',
                 row_width: int = 3) -> ReplyKeyboardMarkup:
    """
        Generate keyboard with pattern with need sturcture
    """
    markup = ReplyKeyboardMarkup(one_time_keyboard=one_time_keyboard,
                                 resize_keyboard=resize_keyboard,
                                 row_width=row_width,
                                 input_field_placeholder=input_field_placegolder)

    for row in markup_pattern:

        row_buttons = []

        for button_text in row:
            row_buttons.append(KeyboardButton(text=button_text))

        markup.add(*row_buttons)

    return markup

