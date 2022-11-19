import sys
import time
import sqlite3
import datetime as dt

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QSplashScreen, QMainWindow


class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()
        uic.loadUi('MonParis.ui', self)

        #кнопки во вкладке профиля
        self.push_profile.clicked.connect(self.window_profile)
        self.push_menu.clicked.connect(self.window_menu)
        self.push_basket.clicked.connect(self.window_basket)
        self.save.clicked.connect(self.save_all)
        self.count = list(map(int, ['0' for i in range(34)]))

        #кнопки во вкладке меню

        #Цезарь с куриной грудкой
        self.pushButton_350.clicked.connect(self.add_food_1)
        #Цезарь с креветками
        self.pushButton_410.clicked.connect(self.add_food_2)
        #Тёплый мясной салат
        self.pushButton_390.clicked.connect(self.add_food_3)
        #Оливье по-французски
        self.pushButton_370.clicked.connect(self.add_food_4)
        #Тёплый французский салат
        self.pushButton_449.clicked.connect(self.add_food_5)
        #Нисуаз с тунцом
        self.pushButton_470.clicked.connect(self.add_food_6)



        self.sql = sqlite3.connect('registration.db')
        self.cursor = self.sql.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   name TEXT,
                   number TEXT,
                   email TEXT,
                   address TEXT
               )""")
        self.sql.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS menu (
                               title TEXT,
                               price TEXT,
                               count BIGINT,
                               time TEXT
                           )""")
        self.sql.commit()

    def window_profile(self):
        self.stackedWidget_2.setCurrentIndex(0)

    def window_menu(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def window_basket(self):
        self.stackedWidget_2.setCurrentIndex(2)

    def save_all(self):
        name = self.lineEdit.text()
        number = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        address = self.lineEdit_4.text()
        self.cursor.execute("SELECT name FROM users")
        if self.cursor.fetchone() is None:
            self.cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (name, number, email, address))
            self.sql.commit()
        else:
            self.label_8.setText('Пользователь уже зарегестрирован')

    # Цезарь с куриной грудкой
    def add_food_1(self):
        time = dt.datetime.now().strftime('%H:%M')
        self.count[0] = self.count[0] + 1
        self.cursor.execute("SELECT title FROM menu WHERE price = '350₽'")
        result = self.cursor.fetchone()
        if result != ('Цезарь с куриной грудкой',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?, ?)",
                                ('Цезарь с куриной грудкой', '350₽', self.count[0], time))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET count = {self.count[0]}
            WHERE title = 'Цезарь с куриной грудкой'""")
            self.sql.commit()

    # Цезарь с креветками
    def add_food_2(self):
        time = dt.datetime.now().strftime('%H:%M')
        self.count[1] = self.count[1] + 1
        self.cursor.execute("SELECT title FROM menu WHERE price = '410₽'")
        result = self.cursor.fetchone()
        if result != ('Цезарь с креветками',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?, ?)",
                                ('Цезарь с креветками', '410₽', self.count[1], time))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET count = {self.count[1]}
            WHERE title = 'Цезарь с креветками'""")
            self.sql.commit()

    # Тёплый мясной салат
    def add_food_3(self):
        time = dt.datetime.now().strftime('%H:%M')
        self.count[2] = self.count[2] + 1
        self.cursor.execute("SELECT title FROM menu WHERE price = '390₽'")
        result = self.cursor.fetchone()
        if result != ('Тёплый мясной салат',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?, ?)",
                                ('Тёплый мясной салат', '390₽', self.count[2], time))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET count = {self.count[2]}
            WHERE title = 'Тёплый мясной салат'""")
            self.sql.commit()

    #Оливье по-французски
    def add_food_4(self):
        time = dt.datetime.now().strftime('%H:%M')
        self.count[3] = self.count[3] + 1
        self.cursor.execute("SELECT title FROM menu WHERE price = '370₽'")
        result = self.cursor.fetchone()
        if result != ('Оливье по-французски',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?, ?)",
                                ('Оливье по-французски', '370₽', self.count[3], time))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET count = {self.count[3]}
            WHERE title = 'Оливье по-французски'""")
            self.sql.commit()

    #Тёплый французский салат
    def add_food_5(self):
        time = dt.datetime.now().strftime('%H:%M')
        self.count[4] = self.count[4] + 1
        self.cursor.execute("SELECT title FROM menu WHERE price = '449₽'")
        result = self.cursor.fetchone()
        if result != ('Тёплый французский салат',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?, ?)",
                                ('Тёплый французский салат', '449₽', self.count[4], time))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET count = {self.count[4]}
            WHERE title = 'Тёплый французский салат'""")
            self.sql.commit()

    # Нисуаз с тунцом
    def add_food_6(self):
        time = dt.datetime.now().strftime('%H:%M')
        self.count[5] = self.count[5] + 1
        self.cursor.execute("SELECT title FROM menu WHERE price = '470₽'")
        result = self.cursor.fetchone()
        if result != ('Нисуаз с тунцом',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?, ?)",
                                ('Нисуаз с тунцом', '470₽', self.count[5], time))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET count = {self.count[5]}
            WHERE title = 'Нисуаз с тунцом'""")
            self.sql.commit()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = QSplashScreen(QPixmap('img.png'))
    splash.showMessage('Загрузка данных...',
                       Qt.AlignHCenter | Qt.AlignBottom, Qt.gray)
    splash.show()
    app.processEvents()
    time.sleep(1)
    ex = Profile()
    ex.show()
    splash.finish(ex)
    sys.exit(app.exec_())

