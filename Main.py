import sys
import time
import sqlite3

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QSplashScreen, QMainWindow


class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()
        uic.loadUi('MonParis.ui', self)

        self.push_profile.clicked.connect(self.window_profile)
        self.push_menu.clicked.connect(self.window_menu)
        self.push_basket.clicked.connect(self.window_basket)
        self.save.clicked.connect(self.save_all)

        self.sql = sqlite3.connect('server.db')
        self.sursor = self.sql.cursor()

        self.sursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   name TEXT,
                   number TEXT,
                   email TEXT,
                   address TEXT
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
        self.sursor.execute("SELECT name FROM users")
        self.sursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (name, number, email, address))
        self.sql.commit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = QSplashScreen(QPixmap('img.png'))
    splash.showMessage('Загрузка данных...',
                       Qt.AlignHCenter | Qt.AlignBottom, Qt.gray)
    splash.show()
    app.processEvents()
    time.sleep(3)
    ex = Profile()
    ex.show()
    splash.finish(ex)
    sys.exit(app.exec_())

