class Car:
    def __init__(self, name):
        self.color = "red"
        self.price = 2000000
        self.name = name


class Human:
    def __init__(self, name, car):
        self.age = 25
        self.name = name
        self.car = car

    def change_color(self):
        print(f'цвет был - {self.car.color}')
        self.car.color = 'green'
        print(f'цвет стал - {self.car.color}')


mers = Car(name='Мерс')
vova = Human(name='Вова', car=mers)
vova.change_color()
# Вот тут человек Никита может менять цвет машины Аносова с красного на синий))))))
# КАААААААААААААК???????!!!!!!
