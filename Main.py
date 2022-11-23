import sys
import time
import sqlite3
import datetime as dt

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QSplashScreen, QMainWindow


class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()
        uic.loadUi('MonParis.ui', self)
        self.stackedWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.label_7.clear()

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
                                       Блюдо TEXT,
                                       Цена TEXT,
                                       Количество TEXT
                                   )""")
        self.sql.commit()

        self.cursor.execute("SELECT name FROM users")
        if self.cursor.fetchone():
            self.cursor.execute("SELECT name FROM users")
            a = self.cursor.fetchone()
            self.lineEdit.setText(*a)

            self.cursor.execute("SELECT number FROM users")
            a = self.cursor.fetchone()
            self.lineEdit_2.setText(*a)

            self.cursor.execute("SELECT email FROM users")
            a = self.cursor.fetchone()
            self.lineEdit_3.setText(*a)

            self.cursor.execute("SELECT address FROM users")
            a = self.cursor.fetchone()
            self.lineEdit_4.setText(*a)

            self.label_8.setText(f'Здравствуйте, {self.lineEdit.text()}')
        else:
            self.label_8.setText('Пользователь не зарегестрирован')

        self.exit.clicked.connect(self.exits)





        # кнопки во вкладке профиля
        self.push_profile.clicked.connect(self.window_profile)
        self.push_menu.clicked.connect(self.window_menu)
        self.push_basket.clicked.connect(self.window_basket)
        self.save.clicked.connect(self.save_all)
        self.count = list(map(int, ['0' for i in range(34)]))

        # кнопки во вкладке меню:
        self.pushButton_350.clicked.connect(self.add_food_1)
        self.pushButton_410.clicked.connect(self.add_food_2)
        self.pushButton_390.clicked.connect(self.add_food_3)
        self.pushButton_370.clicked.connect(self.add_food_4)
        self.pushButton_449.clicked.connect(self.add_food_5)
        self.pushButton_470.clicked.connect(self.add_food_6)
        self.pushButton_380.clicked.connect(self.add_food_7)
        self.pushButton_320.clicked.connect(self.add_food_8)
        self.pushButton_285.clicked.connect(self.add_food_9)
        self.pushButton_310.clicked.connect(self.add_food_10)
        self.pushButton_280.clicked.connect(self.add_food_11)
        self.pushButton_393.clicked.connect(self.add_food_12)
        self.pushButton_605.clicked.connect(self.add_food_13)
        self.pushButton_450.clicked.connect(self.add_food_14)
        self.pushButton_560.clicked.connect(self.add_food_15)
        self.pushButton_336.clicked.connect(self.add_food_16)
        self.pushButton_480.clicked.connect(self.add_food_17)
        self.pushButton_540.clicked.connect(self.add_food_18)
        self.pushButton_768.clicked.connect(self.add_food_19)
        self.pushButton_585.clicked.connect(self.add_food_20)
        self.pushButton_570.clicked.connect(self.add_food_21)
        self.pushButton_360.clicked.connect(self.add_food_22)
        self.pushButton_448.clicked.connect(self.add_food_23)
        self.pushButton_210.clicked.connect(self.add_food_24)
        self.pushButton_140.clicked.connect(self.add_food_25)
        self.pushButton_150.clicked.connect(self.add_food_26)
        self.pushButton_80.clicked.connect(self.add_food_27)
        self.pushButton_100.clicked.connect(self.add_food_28)
        self.pushButton_120.clicked.connect(self.add_food_29)
        self.pushButton_105.clicked.connect(self.add_food_30)
        self.pushButton_155.clicked.connect(self.add_food_31)
        self.pushButton_180.clicked.connect(self.add_food_32)
        self.pushButton_200.clicked.connect(self.add_food_33)
        self.pushButton_160.clicked.connect(self.add_food_34)

        #кнопка на вкладке корзина
        self.order.clicked.connect(self.ordered)

        # Зададим тип базы данных
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        self.db.setDatabaseName('registration.db')
        # И откроем подключение
        self.db.open()

        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)

    def exits(self):
        self.cursor.execute("DELETE from users")
        self.sql.commit()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.label_8.setText('Пользователь не зарегестрирован')


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
                if (name == '') or (number == '') or (email == '') or (address == ''):
                    self.label_8.setText('Заполните все поля')
                else:
                    self.cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (name, number, email, address))
                    self.sql.commit()
                    self.label_8.setText(f'Здравствуйте, {self.lineEdit.text()}')
            else:
                self.label_8.setText('Пользователь уже зарегестрирован')


    def ordered(self):
        self.cursor.execute("SELECT name, number, email, address FROM users")
        if self.cursor.fetchall() and self.cursor.execute("SELECT * FROM menu").fetchall():
            self.cursor.execute("DELETE from menu")
            self.sql.commit()
            self.model = QSqlTableModel(self, self.db)
            self.model.setTable('menu')
            self.model.select()
            self.tableView.setModel(self.model)
            self.tableView.setColumnWidth(0, 160)
            self.tableView.setColumnWidth(1, 30)
            self.tableView.setColumnWidth(2, 76)
            self.label_7.setText('Ожидайте ваш заказ :)')
        elif (self.cursor.execute("SELECT name FROM users").fetchone() is None):
            self.label_7.setText('Вы не авторизованы :(')
        elif self.cursor.execute("SELECT name FROM users").fetchone() \
                and self.cursor.execute("SELECT * FROM menu").fetchone() is None:
            self.label_7.setText('Вы что-то забыли :)')

    # Цезарь с куриной грудкой
    def add_food_1(self):
        self.count[0] = self.count[0] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '350₽'")
        result = self.cursor.fetchone()
        if result != ('Цезарь с куриной грудкой',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Цезарь с куриной грудкой', '350₽', self.count[0]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[0]}
            WHERE Блюдо = 'Цезарь с куриной грудкой'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    # Цезарь с креветками
    def add_food_2(self):
        self.count[1] = self.count[1] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '410₽'")
        result = self.cursor.fetchone()
        if result != ('Цезарь с креветками',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Цезарь с креветками', '410₽', self.count[1]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[1]}
            WHERE Блюдо = 'Цезарь с креветками'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    # Тёплый мясной салат
    def add_food_3(self):
        self.count[2] = self.count[2] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '390₽'")
        result = self.cursor.fetchone()
        if result != ('Тёплый мясной салат',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Тёплый мясной салат', '390₽', self.count[2]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[2]}
            WHERE Блюдо = 'Тёплый мясной салат'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    # Оливье по-французски
    def add_food_4(self):
        self.count[3] = self.count[3] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '370₽'")
        result = self.cursor.fetchone()
        if result != ('Оливье по-французски',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Оливье по-французски', '370₽', self.count[3]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[3]}
            WHERE Блюдо = 'Оливье по-французски'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()


    # Тёплый французский салат
    def add_food_5(self):
        self.count[4] = self.count[4] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '449₽'")
        result = self.cursor.fetchone()
        if result != ('Тёплый французский салат',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Тёплый французский салат', '449₽', self.count[4]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[4]}
            WHERE Блюдо = 'Тёплый французский салат'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    # Нисуаз с тунцом
    def add_food_6(self):
        self.count[5] = self.count[5] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '470₽'")
        result = self.cursor.fetchone()
        if result != ('Нисуаз с тунцом',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Нисуаз с тунцом', '470₽', self.count[5]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[5]}
            WHERE Блюдо = 'Нисуаз с тунцом'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    #Луковый суп
    def add_food_7(self):
        self.count[6] = self.count[6] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '380₽'")
        result = self.cursor.fetchone()
        if result != ('Луковый суп',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Луковый суп', '380₽', self.count[6]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[6]}
            WHERE Блюдо = 'Луковый суп'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    #Томатный суп
    def add_food_8(self):
        self.count[7] = self.count[7] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '320₽'")
        result = self.cursor.fetchone()
        if result != ('Томатный суп',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Томатный суп', '320₽', self.count[7]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[7]}
            WHERE Блюдо = 'Томатный суп'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    #Суп со шпинатом
    def add_food_9(self):
        self.count[8] = self.count[8] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '285₽'")
        result = self.cursor.fetchone()
        if result != ('Суп со шпинатом',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Суп со шпинатом', '285₽', self.count[8]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[8]}
            WHERE Блюдо = 'Суп со шпинатом'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    #Венгерский суп гуляш
    def add_food_10(self):
        self.count[9] = self.count[9] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '310₽'")
        result = self.cursor.fetchone()
        if result != ('Венгерский суп гуляш',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Венгерский суп гуляш', '310₽', self.count[9]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[9]}
            WHERE Блюдо = 'Венгерский суп гуляш'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    #Грибной крем-суп
    def add_food_11(self):
        self.count[10] = self.count[10] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '280₽'")
        result = self.cursor.fetchone()
        if result != ('Грибной крем-суп',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Грибной крем-суп', '280₽', self.count[10]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[10]}
            WHERE Блюдо = 'Грибной крем-суп'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    #Потофе
    def add_food_12(self):
        self.count[11] = self.count[11] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '393₽'")
        result = self.cursor.fetchone()
        if result != ('Потофе',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Потофе', '393₽', self.count[11]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[11]}
            WHERE Блюдо = 'Потофе'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_13(self):
        self.count[12] = self.count[12] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '605₽'")
        result = self.cursor.fetchone()
        if result != ('Утка с яблоками',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Утка с яблоками', '605₽', self.count[12]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[12]}
            WHERE Блюдо = 'Утка с яблоками'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_14(self):
        self.count[13] = self.count[13] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '450₽'")
        result = self.cursor.fetchone()
        if result != ('Кассуле',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Кассуле', '450₽', self.count[13]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[13]}
            WHERE Блюдо = 'Кассуле'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_15(self):
        self.count[14] = self.count[14] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '560₽'")
        result = self.cursor.fetchone()
        if result != ('Беф-бургиньон',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Беф-бургиньон', '560₽', self.count[14]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[14]}
            WHERE Блюдо = 'Беф-бургиньон'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_16(self):
        self.count[15] = self.count[15] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '336₽'")
        result = self.cursor.fetchone()
        if result != ('Куриное филе в травах',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Куриное филе в травах', '336₽', self.count[15]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[15]}
            WHERE Блюдо = 'Куриное филе в травах'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_17(self):
        self.count[16] = self.count[16] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '480₽'")
        result = self.cursor.fetchone()
        if result != ('Форель по-бретонски',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Форель по-бретонски', '480₽', self.count[16]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
            SET Количество = {self.count[16]}
            WHERE Блюдо = 'Форель по-бретонски'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_18(self):
        self.count[17] = self.count[17] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '540₽'")
        result = self.cursor.fetchone()
        if result != ('Рёбра с картофелем',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Рёбра с картофелем', '540₽', self.count[17]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[17]}
               WHERE Блюдо = 'Рёбра с картофелем'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_19(self):
        self.count[18] = self.count[18] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '768₽'")
        result = self.cursor.fetchone()
        if result != ('Сырная тарелка',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Сырная тарелка', '768₽', self.count[18]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[18]}
               WHERE Блюдо = 'Сырная тарелка'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_20(self):
        self.count[19] = self.count[19] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '585₽'")
        result = self.cursor.fetchone()
        if result != ('Мясная тарелка',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Мясная тарелка', '585₽', self.count[19]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[19]}
               WHERE Блюдо = 'Мясная тарелка'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_21(self):
        self.count[20] = self.count[20] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '570₽'")
        result = self.cursor.fetchone()
        if result != ('Пивная тарелка',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Пивная тарелка', '570₽', self.count[20]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[20]}
               WHERE Блюдо = 'Пивная тарелка'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_22(self):
        self.count[21] = self.count[21] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '360₽'")
        result = self.cursor.fetchone()
        if result != ('Лодочка с сыром и яйцом',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Лодочка с сыром и яйцом', '360₽', self.count[21]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[21]}
               WHERE Блюдо = 'Лодочка с сыром и яйцом'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_23(self):
        self.count[22] = self.count[22] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '448₽'")
        result = self.cursor.fetchone()
        if result != ('Фоккачча',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Фоккачча', '448₽', self.count[22]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[22]}
               WHERE Блюдо = 'Фоккачча'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_24(self):
        self.count[23] = self.count[23] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '210₽'")
        result = self.cursor.fetchone()
        if result != ('Брускета с лососем',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Брускета с лососем', '210₽', self.count[23]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[23]}
               WHERE Блюдо = 'Брускета с лососем'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_25(self):
        self.count[24] = self.count[24] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '140₽'")
        result = self.cursor.fetchone()
        if result != ('Капучино',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Капучино', '140₽', self.count[24]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[24]}
               WHERE Блюдо = 'Капучино'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_26(self):
        self.count[25] = self.count[25] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '150₽'")
        result = self.cursor.fetchone()
        if result != ('Латте',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Латте', '150₽', self.count[25]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[25]}
               WHERE Блюдо = 'Латте'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_27(self):
        self.count[26] = self.count[26] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '80₽'")
        result = self.cursor.fetchone()
        if result != ('Эспрессо',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Эспрессо', '80₽', self.count[26]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[26]}
               WHERE Блюдо = 'Эспрессо'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_28(self):
        self.count[27] = self.count[27] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '100₽'")
        result = self.cursor.fetchone()
        if result != ('Макиато',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Макиато', '100₽', self.count[27]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[27]}
               WHERE Блюдо = 'Макиато'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_29(self):
        self.count[28] = self.count[28] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '120₽'")
        result = self.cursor.fetchone()
        if result != ('Доппио',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Доппио', '120₽', self.count[28]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[28]}
               WHERE Блюдо = 'Макиато'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_30(self):
        self.count[29] = self.count[29] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '105₽'")
        result = self.cursor.fetchone()
        if result != ('Американо',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Американо', '105₽', self.count[29]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[29]}
               WHERE Блюдо = 'Американо'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_31(self):
        self.count[30] = self.count[30] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '155₽'")
        result = self.cursor.fetchone()
        if result != ('Флэт Уайт',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Флэт Уайт', '155₽', self.count[30]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[30]}
               WHERE Блюдо = 'Флэт Уайт'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_32(self):
        self.count[31] = self.count[31] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '180₽'")
        result = self.cursor.fetchone()
        if result != ('Халва латте',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Халва латте', '180₽', self.count[31]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[31]}
               WHERE Блюдо = 'Халва латте'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_33(self):
        self.count[32] = self.count[32] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '200₽'")
        result = self.cursor.fetchone()
        if result != ('Арахисовый латте',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Арахисовый латте', '200₽', self.count[32]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[32]}
               WHERE Блюдо = 'Арахисовый латте'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()

    def add_food_34(self):
        self.count[33] = self.count[33] + 1
        self.cursor.execute("SELECT Блюдо FROM menu WHERE Цена = '200₽'")
        result = self.cursor.fetchone()
        if result != ('Раф',):
            self.cursor.execute(f"INSERT INTO menu VALUES (?, ?, ?)",
                                ('Раф', '200₽', self.count[33]))
            self.sql.commit()
        else:
            self.cursor.execute(f"""UPDATE menu
               SET Количество = {self.count[33]}
               WHERE Блюдо = 'Раф'""")
            self.sql.commit()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('menu')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 160)
        self.tableView.setColumnWidth(1, 30)
        self.tableView.setColumnWidth(2, 76)
        self.label_7.clear()



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
