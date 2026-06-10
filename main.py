from os import getenv 
import asyncio 
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import start, menu
from middlewares.sub_checking import SubscribeMiddleware

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(start.router)
dp.include_router(menu.router)


async def main():
    bot = Bot(token=TOKEN)

    dp.message.middleware(SubscribeMiddleware())
    dp.callback_query.middleware(SubscribeMiddleware())

    print("Start bot")
    await dp.start_polling(bot) 

if __name__ == "__main__":
    asyncio.run(main()) 