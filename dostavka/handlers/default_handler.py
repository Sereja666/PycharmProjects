import re

from dostavka.misc import dp, bot, scheduler
from aiogram import types

from dostavka.dostavka_main import gde_tovar


# ... и замените её на:
# from misc import dp


@dp.message_handler(commands=[''])
async def process_where_command(message: types.Message):
    for i in gde_tovar():
        # await send_message_to_all()
        await message.answer(i)
        # await bot.send_message(message.from_user.id, f'message.from_user.id {message.from_user.id}')


@dp.message_handler(content_types=types.ContentTypes.TEXT, state="*")
async def all_other_messages(message: types.Message):
    user_message = message.text
    user_message = user_message.lower()  # привожу всё к мелким буквам
    if re.search(r'\bкек\b', user_message):
        await message.answer("чебурек")


async def where_card():
    # await bot.send_message('-100 558251543','hi there')
    tovar_txt = gde_tovar()
    if tovar_txt is not False:
        for i in tovar_txt:
            await bot.send_message("334892317", i)

# ___________________________________________________________________________________________________________
