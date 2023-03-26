from services.bot.markups.generating_markups import reply_markup
from services.constants.markups import MARKUP_MAIN_MENU
from services.constants.texts import PRESS_ONE_ONE_BELOW_BUTTON


def markup_main_menu():
    return reply_markup(MARKUP_MAIN_MENU, 
                        one_time_keyboard=False,
                        input_field_placegolder=PRESS_ONE_ONE_BELOW_BUTTON)

