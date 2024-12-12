from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == 'test knopka')
async def command_start(message: Message):
    await message.reply(f'Пользователь {message.from_user.full_name}!\n'
                         f'Вы использовали тестовую кнопку!\nОна находтся в разработке!')

@router.message()
async def echo_handler(message: Message):
    try:
        await message.answer('Введите команду, а не случайный текст!')
    except TypeError:
        await message.answer("Nice Try!")