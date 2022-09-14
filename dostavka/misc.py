
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import configparser


config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
bot_token = config['token']['token']


bot = Bot(token=bot_token)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.INFO)
scheduler = AsyncIOScheduler()