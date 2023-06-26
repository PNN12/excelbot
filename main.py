import asyncio
import logging

from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN = "6177439629:AAFS96hc9Fob8IZrdrFls2jH9ncZDLvLxCw"
ADMIN_ID = [202134293, 5619452809, 5858664644, 154509613, 5995852885]
PROG_ID = [154509613, 5995852885]
TEAM_ID = -1001970455550


storage = MemoryStorage()
loop = asyncio.new_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=storage)
logging.basicConfig(level=logging.INFO)

path: str = ""
title: str = ""
flag: bool = True

if __name__ == "__main__":
    
    from handlers import *
    executor.start_polling(dispatcher=dp, skip_updates=True)
