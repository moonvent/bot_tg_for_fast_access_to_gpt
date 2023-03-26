
from telebot.types import CallbackQuery, Message
from bot.commands.start import start
from services.bot.markups.generating_markups import inline_markup
from services.constants.buttons import TO_MAIN_MENU_CALLBACK
from services.constants.markups import INLINE_MARKUP_TO_MAIN_MENU
from bot.util import bot, delete_message


def markup_to_main_menu(row_width: int = 1):
    return inline_markup(INLINE_MARKUP_TO_MAIN_MENU,
                         row_width=row_width)


def __check_to_main_menu_callback(callback: CallbackQuery) -> bool:
    return callback.data == TO_MAIN_MENU_CALLBACK


@bot.callback_query_handler(func=__check_to_main_menu_callback)
def return_to_main_menu(callback: CallbackQuery):
    # delete_message(message_id=callback.message.id,
    #                chat_id=callback.from_user.id)
    chat_id = callback.from_user.id
    bot.clear_step_handler_by_chat_id(chat_id)
    start(chat_id=callback.from_user.id)

