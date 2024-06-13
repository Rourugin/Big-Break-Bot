import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router
from app.database.models import async_main
from commands_menu import set_commands


async def main() -> None:
    await async_main()
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN')) 
    dp = Dispatcher()
    await set_commands(bot)
    print('бот запущен')
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('бот был отключён')