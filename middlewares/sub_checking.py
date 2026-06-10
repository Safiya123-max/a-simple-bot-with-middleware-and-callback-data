from os import getenv 
from dotenv import load_dotenv
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

load_dotenv()
ID = getenv("CHANNEL_ID")
URL = getenv("CHANNEL_URL")


class SubscribeMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        
        bot = data['bot']
        user_id = event.from_user.id

        try:
            member = await bot.get_chat_member(chat_id=ID, user_id=user_id)
            if member.status in ["member", "administrator", "creator"]:
                return await handler(event, data)
            
        except Exception:
            pass
 

        builder = InlineKeyboardBuilder()
        builder.button(text="📢 Subscribe to Channel", url=URL)
        builder.button(text="✅ Check Subscription", callback_data="check_sub_again")
        builder.adjust(1)

        text = ("<b>Before using the Andrew Huberman bot, please subscribe to our channel</b> 👇🏻\n")

        if isinstance(event, CallbackQuery) and event.data == "check_sub_again":
           await event.answer(
           "Bro, you haven't subscribed to all the channels.", 
           show_alert=True)
           return
           
        elif isinstance(event, CallbackQuery):
            try:
                await event.message.delete()
            except Exception:
                pass
            
            await event.message.answer(
                text=text, 
                parse_mode="HTML", 
                reply_markup=builder.as_markup()
            )
            
            await event.answer()
            return

        elif isinstance(event, Message):
            await event.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
        return    
