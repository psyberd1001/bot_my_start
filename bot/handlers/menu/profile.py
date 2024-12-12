from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == 'Профиль')
async def command_start(message: Message):
    await message.reply(f'Пользователь {message.from_user.full_name}!\n'
                         f'Ваш id: {message.from_user.id}')
