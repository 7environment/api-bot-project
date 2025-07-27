from aiogram import F, Router
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent

other = Router()

@other.message()
async def echo(message: Message):
    await message.answer(message.text)