#!venv/bin/python
from aiogram import executor, Bot, Dispatcher, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from misc import scheduler


# from aiogrambot.handlers.Goroskop_Parser import goroskop
from aiogrambot.misc import dp
import aiogrambot.handlers
from aiogrambot.handlers.read_ogg import *

import handlers




if __name__ == "__main__":

    scheduler.start()
    executor.start_polling(dp, skip_updates=True)