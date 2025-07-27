from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

def web_app() -> InlineKeyboardMarkup:
    kb_list = []
    web_app_info = WebAppInfo(url="https://webapp-test-5wv0.onrender.com")
    kb_list.append(
        [InlineKeyboardButton(text="На те яндекс", web_app=web_app_info)]
    )
    return InlineKeyboardMarkup(inline_keyboard=kb_list)