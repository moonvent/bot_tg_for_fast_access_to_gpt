from dataclasses import dataclass
import os
from typing import Iterable, Union
from telebot import TeleBot
from telebot.types import BotCommand, CallbackQuery, Message, BotCommandScope
from services.bot.commands.start_conversation import prepare_text_to_output_in_tg
from services.logs import log


bot = TeleBot(token=os.environ['TOKEN'],
              parse_mode='html')


# bot.set_my_commands([BotCommand(command, description) for command, description in CommandsDescription().get_commands()],
#                     # language_code='ru'
#                     )
# bot.set_my_commands([BotCommand(command, description) for command, description in COMMAND_DESCRIPTIONS_ON_UZB.items()],
#                     language_code='uz')


def start_bot():
    log.critical('Bot Started on POOLING')
    bot.remove_webhook()
    bot.infinity_polling()


def send_message(chat_id: int,
                 text: str,
                 reply_markup=None, 
                 disable_web_page_preview: bool = False,
                 disable_notification: bool = True):

    try:
        bot.send_message(chat_id=chat_id,
                         text=text,
                         reply_markup=reply_markup,
                         disable_web_page_preview=disable_web_page_preview,
                         disable_notification=disable_notification)

    except Exception as e:
        log.error(f'Error in send_message cause - {e}, chat_id - {chat_id}')


@dataclass(frozen=True)
class MessageInfo:
    """
        Store message data with names
    """
    chat_id: int
    text: str
    message_id: int


def get_message_info(message: Union[Message, CallbackQuery],
                     callback_str: str = '') -> MessageInfo:
    """
        Метод для получения данных с сообщения будь-то колбека или обычного
    :param message: необходимое сообщение
    :param callback_str: коллбек начало которое нужно обрезать
    :return: айди, текст, айди сообщения
    """
    if isinstance(message, Message):
        if message.content_type != 'text':
            return MessageInfo(message.from_user.id,
                               message.caption, 
                               message.message_id)
        else:
            return MessageInfo(message.from_user.id,
                               message.text,
                               message.message_id)
    else:
        return MessageInfo(message.from_user.id,
                           message.data[len(callback_str) - 2:],
                           message.message.message_id)


def schedule_message(chat_id: int,
                     text: str,
                     method,
                     reply_markup=None):
    """
        Метод для регистрации следующего шага, чтоб писать меньше строк
    :param reply_markup:
    :param chat_id: кому отправлять
    :param text:    текст сообщения
    :param method:  нужный метод
    :param markup:  нужная клавиатура
    :return:
    """
    try:
        msg = bot.send_message(chat_id=chat_id,
                               text=text,
                               reply_markup=reply_markup)

    except Exception as e:      # если бота заблокировали
        log.error(f'Не удалось отправить сообщение с регистрацией шага из-за ошибки \n {e}')

    else:
        bot.register_next_step_handler(msg, method)
        return msg


def delete_message(chat_id: int,
                   message_id: int):
    """
        Удаление сообщения из канала с отловом эксепшина
    :param chat_id:
    :param message_id:
    :return:
    """
    try:
        bot.delete_message(chat_id=chat_id,
                           message_id=message_id)

    except Exception as e:
        log.error(f'Не удалось удалить сообщение из-за ошибки \n {e}')


def callback_handler(message: CallbackQuery, callback: str) -> bool:
    return message.data.startswith(callback[:-2])


