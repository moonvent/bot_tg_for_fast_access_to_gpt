from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from services.constants.markups import INLINE_MARKUP_STURCTURE, REPLY_MARKUP_STURCTURE


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


def inline_markup(inline_markup_pattern: INLINE_MARKUP_STURCTURE,
                  row_width: int = 3):
    markup = InlineKeyboardMarkup(row_width=row_width)

    for row in inline_markup_pattern:

        row_buttons = []

        for button_text, button_callback in row:
            row_buttons.append(InlineKeyboardButton(text=button_text, 
                                                    callback_data=button_callback))

        markup.add(*row_buttons)

    return markup

