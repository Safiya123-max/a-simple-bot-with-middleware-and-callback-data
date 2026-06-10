from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from keyboards.inline_kb import main_inline


router = Router()


@router.message(Command('start'))
async def start(message: Message):
    photo = FSInputFile('files/photo_1.png')
    caption = (
        "<b>Hey there! Ready to level up your body and mind?</b> 💪\n\n"
        "This bot is a goldmine of science-based insights from Dr. Andrew Huberman! "
        "We’ve got tons of free protocols and guides on how to optimize "
        "your life, master your physical and mental health, and crush your goals.\n"
        "<i>Click below to choose the material you need!</i> 👇"
    )
    await message.answer_photo(
        photo, caption=caption, 
        parse_mode='HTML',
        reply_markup=main_inline()
        )

