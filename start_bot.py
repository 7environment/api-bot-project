import asyncio
import logging
import sys

from src.bot.create import *

from src.bot.handlers.main import register_handlers

register_handlers(dp)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())