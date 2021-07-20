import os
import subprocess
import time

from aiogram import executor, Bot, Dispatcher, types
import schedule
import transliterate
from aiogram import types
import re
import datetime
import asyncio
from contextlib import suppress
# from aiogrambot.handlers.skills import goroskop
# from badwords import *
from pathlib import Path
from aiogram.types import ContentType, File, Message

from aiogrambot.handlers.read_ogg import *
# Если запускаете код отдельно от этого репозитория, то закомментируйте следующую строку:
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from aiogrambot.misc import dp, bot, scheduler

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# ... и замените её на:
# from misc import dp

pronoun = [r"\bя\b", r"\bменя\b", r"\bнас\b", r"\bмы\b", r"\bони\b", r"\bу меня\b"]
drown =  [r"\bзатопили\b", r"\bтопят\b", r"\bзалили\b", r"\bтопим\b", r"\bпотоп\b"]
prodam =  [r"\bпродам\b", r"\bкуплю\b", r"\bпродаю\b"]
curse_words = [
r"\b6ля\b",  r"\bпидорас\b" , r"\b6лядь\b", r"\b6лять\b", r"\bb3ъeб\b", r"\bcock\b", r"\bcunt\b", r"\be6aль\b", r"\bebal\b", r"\beblan\b", r"\beбaл\b", r"\beбaть\b", r"\beбyч\b", r"\beбать\b", r"\beбёт\b", r"\beблантий\b", r"\bfuck\b", r"\bfucker\b", r"\bfucking\b", r"\bxyёв\b", r"\bxyй\b", r"\bxyя\b", r"\bxуе,xуй\b", r"\bxую\b", r"\bzaeb\b", r"\bzaebal\b", r"\bzaebali\b", r"\bzaebat\b", r"\bархипиздрит\b", r"\bахуел\b", r"\bахуеть\b", r"\bбздение\b", r"\bбздеть\b", r"\bбздех\b", r"\bбздецы\b", r"\bбздит\b", r"\bбздицы\b", r"\bбздло\b", r"\bбзднуть\b", r"\bбздун\b", r"\bбздунья\b", r"\bбздюха\b", r"\bбздюшка\b", r"\bбздюшко\b", r"\bбля\b", r"\bблябу\b", r"\bблябуду\b", r"\bбляд\b", r"\bбляди\b", r"\bблядина\b", r"\bблядище\b", r"\bблядки\b", r"\bблядовать\b", r"\bблядство\b", r"\bблядун\b", r"\bблядуны\b", r"\bблядунья\b", r"\bблядь\b", r"\bблядюга\b", r"\bблять\b", r"\bвафел\b", r"\bвафлёр\b", r"\bвзъебка\b", r"\bвзьебка\b", r"\bвзьебывать\b", r"\bвъеб\b", r"\bвъебался\b", r"\bвъебенн\b", r"\bвъебусь\b", r"\bвъебывать\b", r"\bвыблядок\b", r"\bвыблядыш\b", r"\bвыеб\b", r"\bвыебать\b", r"\bвыебен\b", r"\bвыебнулся\b", r"\bвыебон\b", r"\bвыебываться\b", r"\bвыпердеть\b", r"\bвысраться\b", r"\bвыссаться\b", r"\bвьебен\b", r"\bгавно\b", r"\bгавнюк\b", r"\bгавнючка\b", r"\bгамно\b", r"\bгандон\b", r"\bгнид\b", r"\bгнида\b", r"\bгниды\b", r"\bговенка\b", r"\bговенный\b", r"\bговешка\b", r"\bговназия\b", r"\bговнецо\b", r"\bговнище\b", r"\bговно\b", r"\bговноед\b", r"\bговнолинк\b", r"\bговночист\b", r"\bговнюк\b", r"\bговнюха\b", r"\bговнядина\b", r"\bговняк\b", r"\bговняный\b", r"\bговнять\b", r"\bгондон\b", r"\bдоебываться\b", r"\bдолбоеб\b", r"\bдолбоёб\b", r"\bдолбоящер\b", r"\bдрисня\b", r"\bдрист\b", r"\bдристануть\b", r"\bдристать\b", r"\bдристун\b", r"\bдристуха\b", r"\bдрочелло\b", r"\bдрочена\b", r"\bдрочила\b", r"\bдрочилка\b", r"\bдрочистый\b", r"\bдрочить\b", r"\bдрочка\b", r"\bдрочун\b", r"\bе6ал\b", r"\bе6ут\b", r"\bеб твою мать\b", r"\bёб твою мать\b", r"\bёбaн\b", r"\bебaть\b", r"\bебyч\b", r"\bебал\b", r"\bебало\b", r"\bебальник\b", r"\bебан\b", r"\bебанамать\b", r"\bебанат\b", r"\bебаная\b", r"\bёбаная\b", r"\bебанический\b", r"\bебанный\b", r"\bебанныйврот\b", r"\bебаное\b", r"\bебануть\b", r"\bебануться\b", r"\bёбаную\b", r"\bебаный\b", r"\bебанько\b", r"\bебарь\b", r"\bебат\b", r"\bёбат\b", r"\bебатория\b", r"\bебать\b", r"\bебать-копать\b", r"\bебаться\b", r"\bебашить\b", r"\bебёна\b", r"\bебет\b", r"\bебёт\b", r"\bебец\b", r"\bебик\b", r"\bебин\b", r"\bебись\b", r"\bебическая\b", r"\bебки\b", r"\bебла\b", r"\bеблан\b", r"\bебливый\b", r"\bеблище\b", r"\bебло\b", r"\bеблыст\b", r"\bебля\b", r"\bёбн\b", r"\bебнуть\b", r"\bебнуться\b", r"\bебня\b", r"\bебошить\b", r"\bебская\b", r"\bебский\b", r"\bебтвоюмать\b", r"\bебун\b", r"\bебут\b", r"\bебуч\b", r"\bебуче\b", r"\bебучее\b", r"\bебучий\b", r"\bебучим\b", r"\bебущ\b", r"\bебырь\b", r"\bелда\b", r"\bелдак\b", r"\bелдачить\b", r"\bжопа\b", r"\bжопу\b", r"\bзаговнять\b", r"\bзадрачивать\b", r"\bзадристать\b", r"\bзадрота\b", r"\bзае6\b", r"\bзаё6\b", r"\bзаеб\b", r"\bзаёб\b", r"\bзаеба\b", r"\bзаебал\b", r"\bзаебанец\b", r"\bзаебастая\b", r"\bзаебастый\b", r"\bзаебать\b", r"\bзаебаться\b", r"\bзаебашить\b", r"\bзаебистое\b", r"\bзаёбистое\b", r"\bзаебистые\b", r"\bзаёбистые\b", r"\bзаебистый\b", r"\bзаёбистый\b", r"\bзаебись\b", r"\bзаебошить\b", r"\bзаебываться\b", r"\bзалуп\b", r"\bзалупа\b", r"\bзалупаться\b", r"\bзалупить\b", r"\bзалупиться\b", r"\bзамудохаться\b", r"\bзапиздячить\b", r"\bзасерать\b", r"\bзасерун\b", r"\bзасеря\b", r"\bзасирать\b", r"\bзасрун\b", r"\bзахуячить\b", r"\bзаябестая\b", r"\bзлоеб\b", r"\bзлоебучая\b", r"\bзлоебучее\b", r"\bзлоебучий\b", r"\bибанамат\b", r"\bибонех\b", r"\bизговнять\b", r"\bизговняться\b", r"\bизъебнуться\b", r"\bипать\b", r"\bипаться\b", r"\bипаццо\b", r"\bКакдвапальцаобоссать\b", r"\bконча\b", r"\bкурва\b", r"\bкурвятник\b", r"\bлох\b", r"\bлошарa\b", r"\bлошара\b", r"\bлошары\b", r"\bлошок\b", r"\bлярва\b", r"\bмалафья\b", r"\bманда\b", r"\bмандавошек\b", r"\bмандавошка\b", r"\bмандавошки\b", r"\bмандей\b", r"\bмандень\b", r"\bмандеть\b", r"\bмандища\b", r"\bмандой\b", r"\bманду\b", r"\bмандюк\b", r"\bминет\b", r"\bминетчик\b", r"\bминетчица\b", r"\bмлять\b", r"\bмокрощелка\b", r"\bмокрощёлка\b", r"\bмразь\b", r"\bмудak\b", r"\bмудaк\b", r"\bмудаг\b", r"\bмудак\b", r"\bмуде\b", r"\bмудель\b", r"\bмудеть\b", r"\bмуди\b", r"\bмудил\b", r"\bмудила\b", r"\bмудистый\b", r"\bмудня\b", r"\bмудоеб\b", r"\bмудозвон\b", r"\bмудоклюй\b", r"\bна хер\b", r"\bхуй\b", r"\bнабздел\b", r"\bнабздеть\b", r"\bнаговнять\b", r"\bнадристать\b", r"\bнадрочить\b", r"\bнаебать\b", r"\bнаебет\b", r"\bнаебнуть\b", r"\bнаебнуться\b", r"\bнаебывать\b", r"\bнапиздел\b", r"\bнапиздели\b", r"\bнапиздело\b", r"\bнапиздили\b", r"\bнасрать\b", r"\bнастопиздить\b", r"\bнахер\b", r"\bнахрен\b", r"\bнахуй\b", r"\bнахуйник\b", r"\bне ебет\b", r"\bне ебёт\b", r"\bневротебучий\b", r"\bневъебенно\b", r"\bнехира\b", r"\bнехрен\b", r"\bНехуй\b", r"\bнехуйственно\b", r"\bниибацо\b", r"\bниипацца\b", r"\bниипаццо\b", r"\bниипет\b", r"\bникуя\b", r"\bнихера\b", r"\bнихуя\b", r"\bобдристаться\b", r"\bобосранец\b", r"\bобосрать\b", r"\bобосцать\b", r"\bобосцаться\b", r"\bобсирать\b", r"\bобъебос\b", r"\bобьебать обьебос\b", r"\bоднохуйственно\b", r"\bопездал\b", r"\bопизде\b", r"\bопизденивающе\b", r"\bостоебенить\b", r"\bостопиздеть\b", r"\bотмудохать\b", r"\bотпиздить\b", r"\bотпиздячить\b", r"\bотпороть\b", r"\bотъебись\b", r"\bохуевательский\b", r"\bохуевать\b", r"\bохуевающий\b", r"\bохуел\b", r"\bохуенно\b", r"\bохуеньчик\b", r"\bохуеть\b", r"\bохуительно\b", r"\bохуительный\b", r"\bохуяньчик\b", r"\bохуячивать\b", r"\bохуячить\b", r"\bочкун\b", r"\bпадла\b", r"\bпадонки\b", r"\bпадонок\b", r"\bпаскуда\b", r"\bпедерас\b", r"\bпедик\b", r"\bпедрик\b", r"\bпедрила\b", r"\bпедрилло\b", r"\bпедрило\b", r"\bпедрилы\b", r"\bпездень\b", r"\bпездит\b", r"\bпездишь\b", r"\bпездо\b", r"\bпездят\b", r"\bпердануть\b", r"\bпердеж\b", r"\bпердение\b", r"\bпердеть\b", r"\bпердильник\b", r"\bперднуть\b", r"\bпёрднуть\b", r"\bпердун\b", r"\bпердунец\b", r"\bпердунина\b", r"\bпердунья\b", r"\bпердуха\b", r"\bпердь\b", r"\bпереёбок\b", r"\bпернуть\b", r"\bпёрнуть\b", r"\bпи3д\b", r"\bпи3де\b", r"\bпи3ду\b", r"\bпиzдец\b", r"\bпидар\b", r"\bпидарaс\b", r"\bпидарас\b", r"\bпидарасы\b", r"\bпидары\b", r"\bпидор\b", r"\bпидорасы\b", r"\bпидорка\b", r"\bпидорок\b", r"\bпидоры\b", r"\bпидрас\b", r"\bпизда\b", r"\bпиздануть\b", r"\bпиздануться\b", r"\bпиздарваньчик\b", r"\bпиздато\b", r"\bпиздатое\b", r"\bпиздатый\b", r"\bпизденка\b", r"\bпизденыш\b", r"\bпиздёныш\b", r"\bпиздеть\b", r"\bпиздец\b", r"\bпиздит\b", r"\bпиздить\b", r"\bпиздиться\b", r"\bпиздишь\b", r"\bпиздища\b", r"\bпиздище\b", r"\bпиздобол\b", r"\bпиздоболы\b", r"\bпиздобратия\b", r"\bпиздоватая\b", r"\bпиздоватый\b", r"\bпиздолиз\b", r"\bпиздонутые\b", r"\bпиздорванец\b", r"\bпиздорванка\b", r"\bпиздострадатель\b", r"\bпизду\b", r"\bпиздуй\b", r"\bпиздун\b", r"\bпиздунья\b", r"\bпизды\b", r"\bпиздюга\b", r"\bпиздюк\b", r"\bпиздюлина\b", r"\bпиздюля\b", r"\bпиздят\b", r"\bпиздячить\b", r"\bписбшки\b", r"\bписька\b", r"\bписькострадатель\b", r"\bписюн\b", r"\bписюшка\b", r"\bпо хуй\b", r"\bпо хую\b", r"\bподговнять\b", r"\bподонки\b", r"\bподонок\b", r"\bподъебнуть\b", r"\bподъебнуться\b", r"\bпоебать\b", r"\bпоебень\b", r"\bпоёбываает\b", r"\bпоскуда\b", r"\bпосрать\b", r"\bпотаскуха\b", r"\bпотаскушка\b", r"\bпохер\b", r"\bпохерил\b", r"\bпохерила\b", r"\bпохерили\b", r"\bпохеру\b", r"\bпохрен\b", r"\bпохрену\b", r"\bпохуй\b", r"\bпохуист\b", r"\bпохуистка\b", r"\bпохую\b", r"\bпридурок\b", r"\bприебаться\b", r"\bприпиздень\b", r"\bприпизднутый\b", r"\bприпиздюлина\b", r"\bпробзделся\b", r"\bпроблядь\b", r"\bпроеб\b", r"\bпроебанка\b", r"\bпроебать\b", r"\bпромандеть\b", r"\bпромудеть\b", r"\bпропизделся\b", r"\bпропиздеть\b", r"\bпропиздячить\b", r"\bраздолбай\b", r"\bразхуячить\b", r"\bразъеб\b", r"\bразъеба\b", r"\bразъебай\b", r"\bразъебать\b", r"\bраспиздай\b", r"\bраспиздеться\b", r"\bраспиздяй\b", r"\bраспиздяйство\b", r"\bраспроеть\b", r"\bсволота\b", r"\bсволочь\b", r"\bсговнять\b", r"\bсекель\b", r"\bсерун\b", r"\bсерька\b", r"\bсестроеб\b", r"\bсикель\b", r"\bсила\b", r"\bсирать\b", r"\bсирывать\b", r"\bсоси\b", r"\bспиздел\b", r"\bспиздеть\b", r"\bспиздил\b", r"\bспиздила\b", r"\bспиздили\b", r"\bспиздит\b", r"\bспиздить\b", r"\bсрака\b", r"\bсраку\b", r"\bсраный\b", r"\bсранье\b", r"\bсрать\b", r"\bсрун\b", r"\bссака\b", r"\bссышь\b", r"\bстерва\b", r"\bстрахопиздище\b", r"\bсука\b", r"\bсуки\b", r"\bсуходрочка\b", r"\bсучара\b", r"\bсучий\b", r"\bсучка\b", r"\bсучко\b", r"\bсучонок\b", r"\bсучье\b", r"\bсцание\b", r"\bсцать\b", r"\bсцука\b", r"\bсцуки\b", r"\bсцуконах\b", r"\bсцуль\b", r"\bсцыха\b", r"\bсцышь\b", r"\bсъебаться\b", r"\bсыкун\b", r"\bтрахае6\b", r"\bтрахаеб\b", r"\bтрахаёб\b", r"\bтрахатель\b", r"\bублюдок\b", r"\bуебать\b", r"\bуёбища\b", r"\bуебище\b", r"\bуёбище\b", r"\bуебищное\b", r"\bуёбищное\b", r"\bуебк\b", r"\bуебки\b", r"\bуёбки\b", r"\bуебок\b", r"\bуёбок\b", r"\bурюк\b", r"\bусраться\b", r"\bушлепок\b", r"\bх_у_я_р_а\b", r"\bхyё\b", r"\bхyй\b", r"\bхyйня\b", r"\bхамло\b", r"\bхер\b", r"\bхерня\b", r"\bхеровато\b", r"\bхеровина\b", r"\bхеровый\b", r"\bхитровыебанный\b", r"\bхитрожопый\b", r"\bхуeм\b", r"\bхуе\b", r"\bхуё\b", r"\bхуевато\b", r"\bхуёвенький\b", r"\bхуевина\b", r"\bхуево\b", r"\bхуевый\b", r"\bхуёвый\b", r"\bхуек\b", r"\bхуёк\b", r"\bхуел\b", r"\bхуем\b", r"\bхуенч\b", r"\bхуеныш\b", r"\bхуенький\b", r"\bхуеплет\b", r"\bхуеплёт\b", r"\bхуепромышленник\b", r"\bхуерик\b", r"\bхуерыло\b", r"\bхуесос\b", r"\bхуесоска\b", r"\bхуета\b", r"\bхуетень\b", r"\bхуею\b", r"\bхуи\b", r"\bхуй\b", r"\bхуйком\b", r"\bхуйло\b", r"\bхуйня\b", r"\bхуйрик\b", r"\bхуище\b", r"\bхуля\b", r"\bхую\b", r"\bхуюл\b", r"\bхуя\b", r"\bхуяк\b", r"\bхуякать\b", r"\bхуякнуть\b", r"\bхуяра\b", r"\bхуясе\b", r"\bхуячить\b", r"\bцелка\b", r"\bчмо\b", r"\bчмошник\b", r"\bчмырь\b", r"\bшалава\b", r"\bшалавой\b", r"\bшараёбиться\b", r"\bшлюха\b", r"\bшлюхой\b", r"\bшлюшка\b", r"\bябывает",
]





@dp.message_handler(content_types=types.ContentTypes.TEXT, state="*")
async def all_other_messages(message: types.Message):
    ot_polzaka = message.text
    ot_polzaka = ot_polzaka.lower()  # привожу всё к мелким буквам
    if re.search(r'\bкек\b', ot_polzaka):
        await message.answer("чебурек")
    elif re.search(r'\bсписок команд\b', ot_polzaka):  # СПисок команд
        await message.answer("""
        Писать можно маленькими и большими буквами
        1. Список команд
        ++++++++++++++++++++++++++++++++++++++++++
        2. предлагаю ...
        3. Что в списке
        4. Отчисти/сотри/удали список 
        ++++++++++++++++++++++++++++++++++++++++++
        
        Быстрые ответы:
            5. УК Еврейский дом
            6. какой номер аварийки ?  
                Крики о потопе       
            7. какой номер бухгалтерии ?
            8. какой номер юристов ?
  
        
        ++++++++++++++++++++++++++++++
        
        """)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    elif re.search(r'\bпредлагаю\b', ot_polzaka):  # СПисок команд
        res = []
        res.append(message.text)
        text = res[0]
        ogrizok = (text[text.find('предлагаю') + 9:])
        f = open('1.txt', 'a')
        f.write(ogrizok + "\n")
        f.close()
        await message.answer("записал: " + ogrizok)
        # await message.reply("Этот бот принимает только текстовые сообщения!")
    elif re.search(r'\bчто\b', ot_polzaka) and re.search(r'\bв\b', ot_polzaka) and re.search(r'\bсписке\b', ot_polzaka):
        f = open('1.txt', 'r')
        await message.answer("в списке предложений:  ")
        await message.answer(f.read())
        f.close()
    elif re.search(r'\bотчисти список\b', ot_polzaka) or re.search(r'\bсотри список\b', ot_polzaka) or re.search(r'\bудали список\b', ot_polzaka):
        open('1.txt', 'w').close()
        await message.answer("список предложений теперь пуст")

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    elif re.search(r'\bкто дежурит\b', ot_polzaka):
        now = datetime.datetime.now()
        f = open('\\\\hranilka\\AVAGroup\\AVA\\ИТ\\!Общие документы\\графики дежурств\\ДежурствоБота.txt', 'r')
        await message.answer(
            "сегодня " + now.strftime("%d-%m-%Y") + " от рождества Христова. \n " + "     Дежурства:  \n" + f.read())

        f.close()


    elif re.search(r'\bук еврейский\b', ot_polzaka):
        await message.answer(" гавно!  ")


    elif re.search(r'\bкакой\b', ot_polzaka) and re.search(r'\bномер\b', ot_polzaka) and re.search(r'\bбухгалтерии\b', ot_polzaka):
        await message.answer("+79604738776")

    elif re.search(r'\bкакой\b', ot_polzaka) and re.search(r'\bномер\b', ot_polzaka) and re.search(r'\bюристов\b', ot_polzaka):
        await message.answer("+79649128753")

#_Аварийка ___________________________________________________________________________________________________________________________________
    elif re.search(r'\bкакой\b', ot_polzaka) and re.search(r'\bномер\b', ot_polzaka) and re.search(r'\bаварийки\b', ot_polzaka):
        await message.answer("+79384061610")

    for i in pronoun:
        for _ in drown:
            if  re.search(i, ot_polzaka) and re.search(_, ot_polzaka):
                await message.answer("номер аварийки +79384061610")
#----------------------------------------------------------------------------------------------------------------------------------------------

#_Антиреклама _________________________________________________________________________________________________________________________________
    for i in prodam:
            if  re.search(i, ot_polzaka):
                # lastMessageId = message[-1].message_id

                # await bot.delete_message(message.chat.id, message_id=lastMessageId)
                await message.reply(
                    "Реклама в чате запрещена, все предложения по услугам предлагать по ссылке https://forms.gle/fDSsjnCg5fi5S5vRA")

# _Антимат _________________________________________________________________________________________________________________________________
    for word in curse_words:
        if re.search(r'\b{}\b'.format(word), ot_polzaka):

            await message.delete()
            await message.answer( "РОСКОМНАДЗОР удалил ваше сообщение, ребята из отдела \"Э\" уже выехали")




#___________________ Голосовые сообщения в текст ____________________________________________________________________
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


#
# async def send_goroskop(do: Dispatcher):
#     await dp.bot.send_message("проверка повторов")
#
#
# scheduler.add_job(send_goroskop,"cron", hour=16, minute=57 )