from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(F.text == 'О проекте')
async def command_start(message: Message):
    kb_project_url = InlineKeyboardBuilder()
    kb_project_url.row(types.InlineKeyboardButton(
        text="Наш канал", url="https://pwonline.ru/")
    )
    await message.reply(f'Проект будет в скором времени обновляться!', reply_markup=kb_project_url.as_markup())
