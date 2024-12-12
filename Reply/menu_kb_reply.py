from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
def menu_kb() -> ReplyKeyboardMarkup:
    kb_main = ReplyKeyboardBuilder()
    kb_main.button(text='Профиль')
    kb_main.button(text='О проекте')
    kb_main.button(text='test knopka')
    kb_main.adjust(3)
    return kb_main.as_markup(resize_keyboard=True)