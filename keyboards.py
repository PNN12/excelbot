from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from words import *


def get_cancel_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(KeyboardButton(CANCEL))


def get_start_kb() -> ReplyKeyboardMarkup:
    start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
    start_kb.insert(KeyboardButton(DOWNLOAD_EXEL))
    start_kb.insert(KeyboardButton(FIND_VALUES))
    return start_kb
