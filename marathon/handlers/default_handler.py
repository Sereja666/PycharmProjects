import re

from delivery.misc import dp, bot
from aiogram import types

from delivery.delivery_def import where_product
from aiogram.types import ContentTypes, Message
from marathon.bot_tools.chatGPT_for_bot import chat_bot
# ... и замените её на:
# from misc import dp

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("""
        Писать можно маленькими и большими буквами
        1. Список команд
        ++++++++++++++++++++++++++++++++++++++++++
        2. предлагаю ...
        3. Что в списке
        4. Отчисти/сотри/удали список 
        ++++++++++++++++++++++++++++++++++++++++++
        Быстрые ответы:
            5. УК Еврейский дом
            6. какой номер аварийки, бухгалтерии, юристов , сантехник, электрик,  ?           
            7. Крики о потопе и лифте
        /погода
        /гороскоп
        ++++++++++++++++++++++++++++++

        """)


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def doc_handler(message: Message):
    if document := message.document:
        await document.download(
            destination_dir=r"C:\PycharmProjects\delivery\temp"

        )

@dp.message_handler(commands=[''])
async def process_where_command(message: types.Message):
    for i in where_product():
        await message.answer(i)
        # await bot.send_message(message.from_user.id, f'message.from_user.id {message.from_user.id}')


@dp.message_handler(content_types=types.ContentTypes.TEXT, state="*")
async def all_other_messages(message: types.Message):

    user_message = message.text
    if '*' in user_message:
        print(user_message)
        anwser = chat_bot(user_message)
        print(anwser)
        # await bot.send_message("334892317", anwser)
        await message.answer(anwser)


async def where_card():
    product_txt = where_product()

    if product_txt is not False:
        await bot.send_message("334892317", '----------------------------------------------------')
        for i in product_txt:
            await bot.send_message("334892317", i)

# ___________________________________________________________________________________________________________
@dp.message_handler(commands=['чат'])
async def process_chat_id(message: types.Message):
    await message.reply(message.chat.id)
    await bot.send_message("334892317", message.chat.id)