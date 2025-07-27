from src.bot.handlers.admin.main import admin
from src.bot.handlers.user.main import user
from src.bot.handlers.fsm.main import fsm
from src.bot.handlers.other.main import other
from aiogram import Dispatcher

def register_handlers(dp: Dispatcher) -> None:
    dp.include_routers(admin, user, fsm, other)