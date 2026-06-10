from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_inline():
   keyboard = InlineKeyboardMarkup(
     inline_keyboard= [
       [InlineKeyboardButton(text='⚡ Choose material', callback_data="material")]
     ]
   )
   return keyboard

def back_inline():
    keyboard = InlineKeyboardMarkup(
     inline_keyboard= [
       [InlineKeyboardButton(text='⬅️ Back to menu', callback_data="back")]
     ]
   )
    return keyboard



class CategoryClick(CallbackData, prefix="huberman_cat"):
    topic_id: str

def menu_inline():
    builder = InlineKeyboardBuilder()

    categories = [
        ("🧊 Cold Plunges", "cold"),
        ("🏋️ Fitness", "fitness"),
        ("☀️ Light Exposure", "light"),
        ("🧠 Neuroplasticity", "neuro"),
        ("🌙 Sleep Hygiene", "sleep"),
        ("💊 Supplements", "supps")
    ]

    for text, topic in categories:
        builder.button(
            text=text, 
            callback_data=CategoryClick(topic_id=topic).pack()
        )

    builder.adjust(2)
    return builder.as_markup()    

