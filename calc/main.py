from PyQt5 import QtWidgets, QtCore, QtGui
import disigne  # Это наш конвертированный файл дизайна
from disigne import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
import shutil, os, sys, subprocess, time

class ExampleApp(QtWidgets.QMainWindow, disigne.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.init_UI()  # имя в Титуле

    def init_UI(self):  # имя в Титуле
        self.setWindowTitle("Новый человечек")


        self.ui.b1.clicked.connect(self.num1)

    def num1(self):
        self.ui.monitor.appendPlainText("1")



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложен ие


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
