import configparser
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler


config = configparser.ConfigParser()
config.read('config.ini')
bot_id = config["bot_id"]["bot_id"]


bot = Bot(token=bot_id)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.INFO)
scheduler = AsyncIOScheduler()