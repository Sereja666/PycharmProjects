import requests
from aiogrambot.handlers.read_ogg import *
from aiogrambot.misc import dp, bot, scheduler
from aiogrambot.handlers.goroskop_Parser import goroskop
from aiogrambot.handlers.parser_pogoda import weather
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from misc import scheduler
from datetime import datetime

# from aiogram import Dispatcher


# ... и замените её на:
# from misc import dp

pronoun = ["\bя\b", "нас", "мы", "они", "меня"]
drown = ["затоп", "топят", "залил", "топим", "потоп"]
prodam = [r"\bпродам\b", r"\bкуплю\b", r"\bпродаю\b"]
word_broken = ["слом", 'не работает', 'сдох']
curse_words = [
    "6ля", "пидорас", "6лядь", "6лять", "cock", "e6aль", "ebal", "eblan", "eбaл", "eбaть", "eбyч", "eбать",
    "eбёт", "eблантий", "fuck", "fucker", "fucking",
    "xyёв", "\bxyй\b", "xyя", "xуй", "zaeb", "zaebal", "zaebali", "zaebat", "архипиздрит", "ахуел", "ахуеть",
    "бля",
    "вафел", "вафлёр", "взъебка", "взьебка", "взьебывать", "въеб", "въебался", "въебенн", "въебусь", "въебывать",
    "выеб", "выебать", "выебен", "выебнулся", "выебон", "выебываться", "выпердеть", "выссаться", "вьебен", "гавнюк",
    "гавнючка", "гандон", "говенка", "говешка", "говназия", "говноед", "говнолинк", "говночист", "говнюха", "говнядина",
    "говняк", "говняный", "говнять",
    "гондон", "доебываться", "долбоеб", "долбоёб", "дрисня", "дристун", "дристуха", "дрочелло", "дрочена",
    "дрочила", "дрочилка", "дрочистый", "дрочить", "дрочка",
    "е6ал", "е6ут", "еб твою мать", "ёб твою мать", "ёбaн", "ебaть", "ебyч", "ебал", "ебало", "ебальник", "ебан",
    "ебанамать", "ебанат", "ебаная", "ёбаная", "ебанический",
    "ебанный", "ебанныйврот", "ебаное", "ебануть", "ебануться", "ёбаную", "ебаный", "ебанько", "ебарь", "ебат", "ёбат",
    "ебатория", "ебать", "ебать-копать", "ебаться",
    "ебёна", "ебет", "ебёт", "ебец", "ебик", "ебин", "ебись", "ебическая", "ебки", "ебла", "еблан", "ебливый", "еблище",
    "ебло", "еблыст", "ебнуть", "ебнуться", "ебня", "ебошить", "ебская", "ебский", "ебтвоюмать", "ебун", "ебут", "ебуч",
    "ебуче",
    "ебучее", "ебучий", "ебучим", "ебущ", "ебырь", "елдак",
    "елдачить", "заговнять", "задрачивать", "задристать", "задрота", "зае6", "заё6", "заеб", "заёб", "заеба", "заебал",
    "заебанец", "заебастая", "заебастый", "заебать", "заебаться", "заебашить",
    "заебистое", "заёбистое", "заебистые", "заёбистые", "заебистый", "заёбистый", "заебись", "заебошить", "заебываться",
    "залуп", "залупа", "залупаться", "залупить", "залупиться", "замудохаться", "запиздячить",
    "засерать", "засерун", "засеря", "засирать", "засрун", "захуячить", "заябестая", "злоеб", "злоебучая", "злоебучее",
    "злоебучий", "ибанамат", "ибонех", "изговнять", "изговняться", "изъебнуться", "\bипать\b",
    "ипаться", "ипаццо", "конча", " лох ", "лошарa", "лошара", "лошары", "лошок", "лярва", "малафья", "манда",
    "мандавошек", "мандавошка", "мандавошки", "мандей",
    "мандень", "мандеть", "мандища", "мандой", "манду", "мандюк", "минет", "минетчик", "минетчица", "млять",
    "мокрощелка", "мокрощёлка", "мразь", "мудak", "мудель", "мудеть",
    "мудил", "мудила", "мудистый", "мудня", "мудоеб", "мудозвон", "мудоклюй",
    "набздел", "набздеть", "наговнять", "надристать", "надрочить", "наебать", "наебет", "наебнуть", "наебнуться",
    "наебывать", "напиздел", "напиздели", "напиздело", "напиздили", "настопиздить",
    "не ебет", "не ебёт", "невротебучий", "невъебенно", "нехира", "ниибацо",
    "ниипацца", "ниипаццо", "ниипет", "никуя", "нихуя", "обосцать", "объебос", "обьебать", "обьебос",
    "опездал", "опизде", "опизденивающе", "остоебенить", "остопиздеть", "отмудохать", "отпиздить", "отпиздячить",
    "отпороть", "отъебись", "охуевательский", "охуевать", "охуевающий", "охуел", "охуенно",
    "охуеньчик", "охуеть", "охуительно", "охуительный", "охуяньчик", "охуячивать", "охуячить", "очкун", "падонки",
    "паскуда", "педерас", "педрик", "педрила", "педрилло", "педрило", "педрилы",
    "пездень", "пездит", "пездишь", "пездо", "пездят", "пердануть", "пердеж", "пердение", "пердеть", "пердильник",
    "перднуть", "пёрднуть", "пердун", "пердунец", "пердунина", "пердунья", "пердуха", "пердь", "переёбок",
    "пернуть", "пёрнуть", "пи3д", "пи3де", "пи3ду", "пиzдец", "пидар", "пидарaс", "пидарас", "пидарасы", "пидары",
    "пидор", "пидорасы", "пидорка", "пидорок", "пидоры", "пидрас", "пизда", "пиздануть", "пиздануться",
    "пиздарваньчик", "пиздато", "пиздатое", "пиздатый", "пизденка", "пизденыш", "пиздёныш", "пиздеть", "пиздец",
    "пиздит", "пиздить", "пиздиться", "пиздишь", "пиздища", "пиздище", "пиздобол", "пиздоболы", "пиздобратия",
    "пиздоватая", "пиздоватый", "пиздолиз", "пиздонутые", "пиздорванец", "пиздорванка", "пиздострадатель", "пизду",
    "пиздуй", "пиздун", "пиздунья", "пизды", "пиздюга", "пиздюк", "пиздюлина", "пиздюля", "пиздят", "пиздячить",
    "писбшки", "писька", "писькострадатель", "писюн", "писюшка",
    "по хую", "подговнять", "подонки", "подъебнуть", "подъебнуться", "поебать", "поебень", "поёбываает", "поскуда",
    "потаскуха", "потаскушка",
    "похуист", "похуистка", "похую", "придурок", "приебаться", "припиздень", "припизднутый", "припиздюлина",
    "пробзделся", "проеб", "проебанка", "проебать", "промандеть", "промудеть", "пропизделся", "пропиздеть",
    "пропиздячить",
    "раздолбай", "разхуячить", "разъеб", "разъеба", "разъебай",
    "разъебать", "распиздай", "распиздеться", "распиздяй", "распиздяйство", "распроеть", "сволота", "сволочь",
    "сговнять", "секель", "серька", "сестроеб", "сикель",
    "сирать", "сирывать", "спиздел", "спиздеть", "спиздил", "спиздит", "спиздить",
    "срака", "сраку", "сраный", "сранье", "срун",
    "ссака", "ссышь", "стерва", "страхопиздище", "сука", "суки", "суходрочка", "сучара", "сучий", "сучка", "сучко",
    "сучонок", "сучье", "сцание", "сцука", "сцуки", "сцуконах",
    "сцуль", "сцыха", "съебаться", "трахае6", "трахаеб", "трахаёб", "трахатель", "ублюдок", "уебать", "уёбищ",
    "уебк", "уебки",
    "уёбки", "уебок", "уёбок", "урюк", "ушлепок", "х_у_я_р_а", "хyё", "\bхyй", "хyйня", "хамло", " хер ", "херня",
    "херовато", "херовина", "херовый", "хитровыебанный",
    "хуeм", "хуевато", "хуёвенький", "хуевина", "хуево", "хуевый", "хуёвый", "хуек", "хуёк", "хуел",
    "хуем", "хуенч", "хуеныш", "хуенький", "хуеплет", "хуеплёт", "хуерик", "хуерыло", "хуесос", "хуесоска", "хуета",
    "хуетень", "хуею", "хуи", "хуй", "хуище", "хуля", " хую ",
    "хуюл", "хуя", "хуяк", "хуякать", "хуякнуть", "хуяра", "хуясе", "хуячить", "целка", "чмо", "чмошник", "чмырь",
    "шалава",
    "шалавой", "шараёбиться", "шлюха", "шлюхой", "шлюшка",
    "ябывает", "ху йня"
]



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


@dp.message_handler(commands=['гороскоп'])
async def process_goroskop(message: types.Message):
    await message.reply(goroskop())



@dp.message_handler(commands=['погода'])
async def process_weather(message: types.Message):
    await message.reply(weather())


@dp.message_handler(commands=['чат'])
async def process_chat_id(message: types.Message):
    await message.reply(message.chat.id)

async def process_message_id(message: types.Message):
    await message.reply(message.message_id)

@dp.message_handler(content_types=types.ContentTypes.TEXT, state="*")
async def all_other_messages(message: types.Message):
    user_message = message.text
    user_message = user_message.lower()  # привожу всё к мелким буквам
    if re.search(r'\bкек\b', user_message):

        await message.answer("чебурек")
        # m_id = int(message.message_id) - 1
        # print(m_id)
        # await bot.delete_message("-544312703", m_id)


    elif re.search(r'\bпредлагаю\b', user_message):  # СПисок команд
        res = []
        res.append(message.text)
        text = res[0]
        ogrizok = (text[text.find('предлагаю') + 9:])
        f = open('1.txt', 'a')
        f.write(ogrizok + "\n")
        f.close()
        await message.answer("записал: " + ogrizok)
        # await message.reply("Этот бот принимает только текстовые сообщения!")
    elif re.search(r'\bчто\b', user_message) and re.search(r'\bв\b', user_message) and re.search(r'\bсписке\b',
                                                                                                 user_message):
        f = open('1.txt', 'r')
        await message.answer("в списке предложений:  ")
        await message.answer(f.read())
        f.close()
    elif re.search(r'\bотчисти список\b', user_message) or re.search(r'\bсотри список\b', user_message) or re.search(
            r'\bудали список\b', user_message):
        open('1.txt', 'w').close()
        await message.answer("список предложений теперь пуст")

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




    elif "номер" in user_message and "бухгалтер" in user_message:
        await message.answer("номер бухгалтерии +79604738776")

    elif "номер" in user_message and "юрист" in user_message:
        await message.answer("номер юристов АСК +79649128753")

    elif "номер" in user_message and "электрик" in user_message:
        await message.answer("Александр Николаевич +79054958821")

    elif "номер" in user_message and "сантехн" in user_message:
        await message.answer("Александр Степанович +79184563346")

    elif "номер" in user_message and "мастер" in user_message and "участк" in user_message:
        await message.answer("Александр Юрьевич +79654624849. По выходным не звонить :) ")

    # elif "сломался" in user_message and "лифт" in user_message:
    #     await message.answer("лифтёры +79180163377")

    elif "номер" in user_message and "участков" in user_message:
        await message.answer("Участковый - 88612372248")

    elif "номер" in user_message and "аварийк" in user_message:
        await message.answer("номер аварийки +79384061610")


    # _ гороскоп                     ___________________________________________________________________________________________________________
    elif "что меня сегодня ждёт" in user_message:
        await message.answer(goroskop())

    # _ проблемы с лифтом                    ___________________________________________________________________________________________________________
    for glagol in word_broken:
        if glagol in user_message and 'лифт' in user_message:
            await message.answer("лифтёры +79180163377")

    # _ меня топят                     ___________________________________________________________________________________________________________
    for mestoimenie in pronoun:
        for glagol in drown:
            if mestoimenie in user_message and glagol in user_message:
                await message.answer("номер аварийки +79384061610")

    # ----------------------------------------------------------------------------------------------------------------------------------------------

    # _Антиреклама _________________________________________________________________________________________________________________________________
    for i in prodam:
        if re.search(i, user_message):
            # lastMessageId = message[-1].message_id

            # await bot.delete_message(message.chat.id, message_id=lastMessageId)
            await message.reply(
                "Реклама в чате запрещена, все предложения по услугам предлагать по ссылке https://forms.gle/fDSsjnCg5fi5S5vRA")

    # _Антимат _________________________________________________________________________________________________________________________________
    for word in curse_words:
        # if re.search(r'\b{}\b'.format(word), user_message):
        if word in user_message:
            await message.delete()
            await message.answer(
                "РОСКОМНАДЗОР удалил ваше сообщение\n  🚓  Статья 20.1. КоАП РФ предусматривает штраф за нецензурную брань в общественном месте 🚓 ")


# ___________________ Голосовые сообщения в текст ____________________________________________________________________
async def handle_file(file: File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")


@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    voice = await message.voice.get_file()
    path = "C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\converter"

    # await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path=path)
    # await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path=path)
    await handle_file(file=voice, file_name=f"1.ogg", path=path)
    await message.answer('Ща переведу ... ')
    bot_answer = BotListen()
    bot_answer.act('C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\converter\\1.ogg')
    # with open('text.txt', "r", encoding="utf-8") as file_good1:
    #     for line in file_good1:
    #         await message.answer(line)
    # await message.answer(file_good1)
    await message.answer(bot_answer.text_out)
    try:
        os.remove('C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\converter\\ready.wav')
    except Exception:
        pass
    try:
        os.remove('C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\converter\\1.ogg')
    except Exception:
        pass
    try:
        os.remove('C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\ready.wav')
    except Exception:
        pass



# отправка сообщений по времени ----------------------------------------------------------------------------
async def send_message_to_all(dp: Dispatcher ):

    try:
        with open('log_message_gproskop.txt', 'r') as f:
            mess_id_del = int(f.read())
            await dp.bot.delete_message(chat_id="-1001322775272", message_id=mess_id_del)
    except Exception:
        print("нечего удалять")

    sent_msg = await dp.bot.send_message(chat_id="-1001322775272", text=goroskop(), disable_notification=True)

    mess_id_del = str(sent_msg.message_id)
    with open('log_message_gproskop.txt', 'w') as f:
        f.write(mess_id_del)

    try:
        with open('log_message_pogoda.txt', 'r') as f:
            mess_id_del = int(f.read())
            await dp.bot.delete_message(chat_id="-1001322775272", message_id=mess_id_del)
    except Exception:
        print("нечего удалять")

    sent_msg = await dp.bot.send_message(chat_id="-1001322775272", text=weather(), disable_notification=True)

    mess_id_del = str(sent_msg.message_id)
    with open('log_message_pogoda.txt', 'w') as f:
        f.write(mess_id_del)

    # await dp.bot.send_message(chat_id="-544312703", text=goroskop(), disable_notification=True)
    # await dp.bot.send_message(chat_id="-1001322775272", text=goroskop(), disable_notification=True)
    # await dp.bot.send_message(chat_id="-1001322775272", text=weather(), disable_notification=True)



def schedule_jobs():
    scheduler.add_job(send_message_to_all, "cron", hour=7, minute=1, args=(dp,))
    # scheduler.add_job(send_message_to_all, "interval", seconds=20, args=(dp,))
# ___________________________________________________________________________________________________________
