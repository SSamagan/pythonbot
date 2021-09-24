from aiogram import Bot, Dispatcher, executor
import asyncio
from config import bot_token as token

loop = asyncio.get_event_loop()
bot = Bot(token, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__=="__main__":
    from handlers import dp, sendmessage
    executor.start_polling(dp, on_startup=sendmessage)