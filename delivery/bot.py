#!venv/bin/python

from aiogram import executor

import warnings

import asyncio


from delivery.handlers.default_handler import *

DELAY = 3600
warnings.filterwarnings("ignore", category=DeprecationWarning)


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, where_card, loop)
    executor.start_polling(dp, skip_updates=False, loop=loop)
