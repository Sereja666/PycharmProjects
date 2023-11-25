# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):

        self.money = 100  # кол-во денег в тумбочке (в начале - 100)
        self.food = 50  # кол-во еды в холодильнике (в начале - 50)
        self.mud = 0  # кол-во грязи (в начале - 0)
        self.money_all = 0
        self.food_all = 0
        self.coat = 0
        self.cat_food = 50

    def pollution(self, citizens):  # не забудьте поправить стиль кода (code/reformat code)
        self.mud += 5
        if self.mud >= 90:
            for hun in citizens:
                hun.happiness -= 10
        if self.mud < 0:
            self.mud = 0

    def __str__(self):
        return 'Денег осталось {}, еды в холодильнике {} едениц, грязи - {}'.format(self.money, self.food, self.mud)


class Human:  # лишние скобки

    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.home = house
        self.live = True
        self.action = True

    def __str__(self):
        return '{} - сыт на {} едениц, счастлив на {}'.format(self.name, self.satiety, self.happiness)

    def eat(self):
        #   с home та же история, нужно обращаться не к конкретной внешней переменной
        #  а к атрибутам класса
        if self.home.food > 0:
            self.home.food -= 30
            self.satiety += 30
            self.home.food_all += 30
            cprint('{} поел'.format(self.name), color='yellow')
            self.action = False
        else:
            cprint('{} помер'.format(self.name), color='red')
            self.live = False

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10
        cprint('{} играл с котейкой'.format(self.name), color='yellow')
        self.action = False

    def act(self):  #
        dice = randint(1, 3)
        if self.satiety < 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            self.live = False

        elif self.happiness < 0:
            cprint('{} умер от дипрессии ...'.format(self.name), color='red')
            self.live = False

        elif self.satiety < 20:
            self.eat()
            self.action = False

        elif dice == 1:
            self.pet_the_cat()
            self.action = False


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 30

        self.home = house
        self.live = True
        self.action = True

    def __str__(self):
        return '{} - сыт на {} едениц'.format(self.name, self.satiety)

    def act(self):
        if self.live is True:
            dice = randint(1, 2)
            if self.satiety < 0:
                cprint('{} умер от голода...'.format(self.name), color='red')
                self.live = False
            elif self.satiety < 20:
                self.eat()
            elif dice == 2:
                self.soil()
            else:
                self.sleep()
        else:
            cprint('{} умер от голода...'.format(self.name), color='red')

    def eat(self):
        if self.home.cat_food > 0:
            self.home.cat_food -= 10
            self.satiety += 20
            self.home.food_all += 10
            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} помер'.format(self.name), color='red')
            self.live = False

    def sleep(self):
        self.satiety -= 10
        cprint('{} спал весь день'.format(self.name), color='yellow')

    def soil(self):
        self.satiety -= 10
        self.home.mud += 5
        cprint('{} точил когти об обои'.format(self.name), color='yellow')


#  В первую очередь можно вынести полностью одинаковые методы, вроде eat
#  В этом случае достаточно просто добавить в родительский класс этот метод и убрать его из наследников

#  Помимо целых действий вроде eat
#  Можно выделять схожие части методов и выносить их в родительский класс
#  Например можно взять общие проверки и действия из act
#  Записать их в act родительского класса, добавив к ним возврат
#  либо True, либо False
#  True - если человек жив и способен выполнить какое-нибудь действие
#  False - если человек мертв или уже выполнил одно из действий
#  В act наследников тогда нужно будет использовать вызов метода через super()
#  и проверить то, что вернёт этот вызов (if super().func())
#  Если возвращается True - продолжать выбор действия, если False - завершать функцию

class Child(Human):
    # # Ребенок может:
    # #   есть,
    # #   спать,
    # #
    # # отличия от взрослых - кушает максимум 10 единиц еды,
    # # степень счастья  - не меняется, всегда ==100 ;)
    def __init__(self, name, house):

        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.live is True:
            if self.satiety <= 30:
                self.eat()
            else:
                self.sleep()
        self.happiness = 100

    def eat(self):
        if self.home.food > 0:
            self.home.food -= 10
            self.satiety += 10
            self.home.food_all += 10
            cprint('{} поел'.format(self.name), color='yellow')
            self.action = False
        else:
            cprint('{} помер'.format(self.name), color='red')
            self.live = False

    def sleep(self):
        self.satiety -= 3
        cprint('{} спал весь день'.format(self.name), color='yellow')
        self.action = False


class Husband(Human):
    # У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100)
    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):

        dice = randint(1, 3)
        super().act()
        if self.live is True and self.action is True:  # лишние скобки
            #  Кстати с объектами вроде True/None/False принято использовать is вместо ==
            #  он работает быстрее
            if self.home.money <= 400:  # везде home надо заменить на self.house
                self.work()
            elif dice == 1:
                self.work()
            elif dice == 2:
                super().eat()
            else:
                self.gaming()

        self.action = True

    def work(self):  # Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
        self.home.money += 500
        self.satiety -= 10
        cprint('{} сходил на работу'.format(self.name), color='yellow')

    def gaming(self):  # Степень счастья растет: у мужа от игры в WoT (на 20)
        self.happiness += 20
        self.satiety -= 10
        cprint('{} тупил в танки весь день'.format(self.name), color='yellow')


class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):  #
        super().act()
        dice = randint(1, 3)
        if self.live is True and self.action is True:
            if self.home.food <= 100:
                self.shopping()
            elif self.home.cat_food <= 100:
                self.shopping()
            elif self.happiness <= 50:
                self.buy_fur_coat()
            elif self.home.mud >= 50:
                self.clean_house()
            elif dice == 2:
                self.shopping()
            else:
                self.pet_the_cat()

        self.action = True

    def shopping(self):
        if self.home.money > 0:
            self.home.food += 200
            self.home.cat_food += 100
            self.home.money -= 300
            self.satiety -= 10
            self.home.money_all += 300
            cprint('{} сходила в пятёрочку купила еды на семью и котейке'.format(self.name), color='yellow')
        else:
            self.satiety -= 10
            self.happiness = -10
            cprint('{} голодает и плачет'.format(self.name), color='yellow')
        self.action = False

    def buy_fur_coat(self):
        if self.home.money > 0:
            self.happiness += 60
            self.home.money -= 350
            self.satiety -= 10
            self.home.coat += 1
            self.home.money_all += 350
            cprint('{} купила шубу'.format(self.name), color='yellow')
            self.action = False
        else:
            self.happiness -= 10
            self.satiety -= 10
            cprint('{} пошла купить шубу, но карту заблокировари, за одно и проголодалась'.format(self.name),
                   color='yellow')
            self.action = False

    def clean_house(self):
        self.home.mud -= 100
        self.satiety -= 10
        cprint('{} помыла всю хату'.format(self.name), color='yellow')
        self.action = False

    # def girls_period(self):  # добавил реалистичности
    #     self.happiness -= 10
    #     self.satiety -= 10
    #     cprint('{} весь день бесила мужа'.format(self.name), color='yellow')
    #     self.action = False


home = House()

citizens = [
    Husband(name="Сережа", house=home),
    Wife(name="Маша", house=home),
    Child(name="Стасик", house=home)
]

murzik = Cat(name="Мурзик", house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')

    for citizen in citizens:
        citizen.act()
        home.pollution(citizens)

    murzik.act()

    for citizen in citizens:
        cprint(citizen, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')

cprint('за год было потраченно денег - {}, съеденно {} кг еды, и купленно {} шуб'.format(home.money_all, home.food_all,
                                                                                         home.coat), color='green')
# TODO после реализации первой части - отдать на проверку учителю

# ######################################################## Часть вторая
# #
# # После подтверждения учителем первой части надо
# # отщепить ветку develop и в ней начать добавлять котов в модель семьи
# #
# # Кот может:
# #   есть,
# #   спать,
# #   драть обои
# #
# # Люди могут:
# #   гладить кота (растет степень счастья на 5 пунктов)
# #
# # В доме добавляется:
# #   еда для кота (в начале - 30)
# #
# # У кота есть имя и степень сытости (в начале - 30)
# # Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# # Еда для кота покупается за деньги: за 10 денег 10 еды.
# # Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# # Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
# #
# # Если кот дерет обои, то грязи становится больше на 5 пунктов
#

#
# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)
#
# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
# # TODO после реализации второй части - отдать на проверку учителем две ветки
#
#
# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#
# # Усложненное задание (делать по желанию)
# #
# # Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# # Коты должны выжить вместе с семьей!
# #
# # Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# # Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
# #
# # Дополнительно вносить некий хаос в жизнь семьи
# # - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# # - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# # Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
# #   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
# #
# # в итоге должен получится приблизительно такой код экспериментов
# # for food_incidents in range(6):
# #   for money_incidents in range(6):
# #       life = Simulation(money_incidents, food_incidents)
# #       for salary in range(50, 401, 50):
# #           max_cats = life.experiment(salary)
# #           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#зачёт!
