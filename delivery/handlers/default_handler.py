import re

from delivery.misc import dp, bot
from aiogram import types

from delivery.delivery_def import where_product


# ... и замените её на:
# from misc import dp


@dp.message_handler(commands=[''])
async def process_where_command(message: types.Message):
    for i in where_product():
        await message.answer(i)
        # await bot.send_message(message.from_user.id, f'message.from_user.id {message.from_user.id}')


@dp.message_handler(content_types=types.ContentTypes.TEXT, state="*")
async def all_other_messages(message: types.Message):
    user_message = message.text
    user_message = user_message.lower()  # привожу всё к мелким буквам
    if re.search(r'\bкек\b', user_message):
        await message.answer("чебурек")


async def where_card():
    product_txt = where_product()

    if product_txt is not False:
        await bot.send_message("334892317", '----------------------------------------------------')
        for i in product_txt:
            await bot.send_message("334892317", i)

# ___________________________________________________________________________________________________________
