import os, shutil, os, sys, stat, subprocess

# from colorama import Fore, Back, Style
#
# colorama.init()


def copy1():
    dir1 = input("что копируем? \n")
    dir2 = input("куда копируем? \n")
    try:
        shutil.copytree(dir1, dir2)
        print("скопированно")
    except FileExistsError:
        dir2 = input("данная папка уже есть, попробуй выбрать другую \n")
        shutil.copytree(dir1, dir2)
        print("скопированно")

def copy2():
    # xcopy /y /o /e "c:\test copy\*.*" "c:\Program Files\test copy\*.*"
    # xcopy /y /o /e "C:\Py\dist\*.*" "C:\Py\dist\1\*.*"

    # / Y - Подавление запроса подтверждения на перезапись существующего конечного файла.
    dir1 = input("что копируем? \n")
    dir2 = input("куда копируем? \n")
    try:
        subprocess.check_output(
            r'C:\Windows\System32\cmd.exe xcopy /y /e /C "{}\*.*" "{}\*.*"'.format(dir1, dir2),
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("сложная ошибка, ещё не разобрался")

def prava():
    dir1 = input("на какую ветку даём права? \n ")
    user = input("кому? \n")
    razreshenia = input("""какие права ? 
    1 - F - полный доступ
    2 - RX - доступ на чтение и выполнение
    3 - RX - доступ на чтение и выполнение ТОЛЬКО в этой папке
    4 - N - доступ отсутствует
    5 - сбросить 
    """)
    if razreshenia == "1":
        subprocess.check_output(
            r'C:\Windows\System32\icacls.exe "{}" /grant "{}":(OI)(CI)(F) /T /C /inheritance:e'.format(dir1, user),
            stderr=subprocess.STDOUT)
    elif razreshenia == "2":
        subprocess.check_output(
            r'C:\Windows\System32\icacls.exe "{}" /grant "{}":(OI)(CI)(RX) /T /C /inheritance:e'.format(dir1, user),
            stderr=subprocess.STDOUT)
    elif razreshenia == "3":
        subprocess.check_output(
            r'C:\Windows\System32\icacls.exe "{}" /grant "{}":(OI)(CI)(RX)  /C /inheritance:e'.format(dir1, user),
            stderr=subprocess.STDOUT)
    elif razreshenia == "4":
        subprocess.check_output(
            r'C:\Windows\System32\icacls.exe "{}" /grant "{}":N /T /C /inheritance:e'.format(dir1, user),
            stderr=subprocess.STDOUT)
    elif razreshenia == "5":
        subprocess.check_output(
            r'C:\Windows\System32\icacls.exe "{}" /reset /T'.format(dir1),
            stderr=subprocess.STDOUT)
        # icacls.exe
        # "M:\Новый ForAll\Агентство по продажам недвижимости\!Документы отдела\" /reset /T
    # subprocess.check_output(
    #     r'C:\Windows\System32\icacls.exe "C:\PyTest\1" /GRANT *S-1-1-0:F',
    #     stderr=subprocess.STDOUT)


# icacls "\\hranilka\AVAGroup\AVA\Строительный департамент АСК\Документы отдела ОКС\!СДО" /grant "ava\Строительный деп АСК_СДО_G_B14":RX /T


def ctovpapke():
    compname = ("имя компа? \n ")
    dir2 = "\\{}\\c$\\Users\\UrkoNS\\Desktop".format(compname)
    dir1 = input("где смотрим? \n ")
    for root, dirs, files in os.walk(dir1):
        print(root)
        for _dir in dirs:
            print(_dir)

        for _file in files:
            print('|_', _file)


while True:
    os.system('CLS')
    vopros = input("""
========================================================================================    
    что будем делать?
        1 - копировать Питон
        2 - копировать CMD
        3 - права
        4 - что в папке?
========================================================================================          
        """)
    if vopros == "1":
        copy1()
    if vopros == "2":
        copy2()
    if vopros == "3":
        prava()
    if vopros == "4":
        ctovpapke()
