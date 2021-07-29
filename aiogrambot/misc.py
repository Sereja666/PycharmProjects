
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

bot = Bot(token="1803871509:AAHQCr3W-iLi3wj7s-V_rBhng4sk5a8v7JE")
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.INFO)
scheduler = AsyncIOScheduler()