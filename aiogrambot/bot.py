#!venv/bin/python
from aiogram import executor, Bot, Dispatcher, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from misc import scheduler


from aiogrambot.misc import dp
from aiogrambot.handlers.default_handler import *
from aiogrambot.handlers.read_ogg import *

# import handlers


async def on_startup(message: types.Message):
    schedule_jobs()

if __name__ == "__main__":

    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
