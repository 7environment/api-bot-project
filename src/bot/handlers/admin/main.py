from aiogram import F, Router
from aiogram.types import Message

from src.bot.keyboards.inline.keyboards import web_app

from src.database.methods.user import add_user
from src.database.create import new_session

from src.exeptions.database import UserAlreadyExistsError, DatabaseError

admin = Router()

@admin.message(F.text == "/start")
async def start_admin(message: Message):
    async with new_session() as session:
        try:
            await add_user(session, message.from_user.id)
            await message.answer("Вот тебе гениальный сайт", reply_markup=web_app())
        except UserAlreadyExistsError:
            await message.answer("С возвращением! Вот ваш сайт", reply_markup=web_app())
        except DatabaseError as e:
            print("\n", str(e))
            await message.answer("Произошла ошибка, напишите администратору @che_za_0iq")
            # Логируй ошибку
            # logger.error("Database error for user %s", message.from_user.id, exc_info=True)