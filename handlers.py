from main import bot, dp
from aiogram.types import Message
from config import id

async def sendmessage(dp):
    await bot.send_message(chat_id=id, text="Привет я бот")

@dp.message_handler()
async def echo(message: Message):
    text = f"Э {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)
    # await message.answer(text=text)