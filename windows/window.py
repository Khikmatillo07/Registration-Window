from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QComboBox
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon, QPixmap
from random import choice
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import requests
import re


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("img/registration.png")
                           )  # oyna chetiga rasm qo'yish
        self.setWindowTitle("Registration")  # Oynani nomlash
        self.setFixedSize(800, 500)  # Oyna shu razmerdan o'zgarmaydi
        self.setStyleSheet("background-color: #5D5DB1")
        self.sarlavxa = QLabel("Бесплатная регистрация", self)  # Yozuv
        self.sarlavxa.setGeometry(250, 30, 470, 30)
        self.sarlavxa.setStyleSheet("color: linen;font-size:25px")

        self.person = QLabel(self)
        person1 = QPixmap("img/user.png").scaled(QtCore.QSize(60, 60))
        self.person.setPixmap(person1)
        self.person.setGeometry(350, 85, 60, 60)
        self.person = QIcon("img/user.png")

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("            Введите имя")
        self.name.setGeometry(275, 180, 230, 35)
        self.name.setStyleSheet(
            "background-color: #20E4B0;font-size:18px;color:white")

        self.email = QLineEdit(self)
        self.email.setPlaceholderText(" Ваш электронный адрес")
        self.email.setGeometry(275, 230, 230, 35)
        self.email.setStyleSheet(
            "background-color: #20E4B0;font-size:18px;color:white")

        self.parol = QLineEdit(self)
        self.parol.setPlaceholderText("        Введите пароль")
        self.parol.setEchoMode(QLineEdit.EchoMode.Password)
        self.parol.setGeometry(275, 285, 230, 35)
        self.parol.setStyleSheet(
            "background-color: #20E4B0;font-size:18px;color:white")

        self.photo = QLineEdit(self)
        self.photo.setPlaceholderText("Введите число с картики")
        self.photo.setGeometry(275, 335, 230, 35)
        self.photo.setStyleSheet(
            "background-color: #20E4B0;font-size:18px;color:white")

        self.rasm = QLabel(self)
        rasm1 = QPixmap("img/rasm.png").scaled(QtCore.QSize(60, 60))
        self.rasm.setPixmap(rasm1)
        self.rasm.setGeometry(190, 335, 70, 35)
        self.rasm = QIcon("img/rasm.png")

        self.parol0 = QCheckBox("Показать пароль", self)
        self.parol0.setGeometry(520, 285, 120, 40)

        self.reg = QPushButton("Зарегистрироваться", self)
        self.reg.setGeometry(310, 400, 170, 35)
        self.reg.setStyleSheet(
            "background-color: #5AC2E3;font-size:18px;color:white")

        self.reg.clicked.connect(self.praver_name)
        self.reg.clicked.connect(self.praver_email)
        self.reg.clicked.connect(self.praver_parol)
        self.reg.clicked.connect(self.send_message_bot)
        self.reg.clicked.connect(self.p_kar)
        self.parol0.clicked.connect(self.sc_parol)

    def sc_parol(self):
        if self.parol0.isChecked():
            self.parol.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.parol.setEchoMode(QLineEdit.EchoMode.Password)

    def praver_n(self):
        name1 = self.name
        return name1.text().isalpha()

    def praver_name(self):
        if self.praver_n():
            pass
        else:
            QMessageBox.critical(self, "Xatolig", "Ism Noto'g'ri kiritildi")
    ####################################################

    def praver_e(self):
        email1 = str(self.email.text())
        return re.match("[a-z0-9]+@+[a-z]+\.+[a-z]", email1)

    def praver_email(self):
        if self.praver_e():
            pass
        else:
            QMessageBox.critical(self, "Xatolig", "Email Noto'g'ri kiritildi")
    ######################################

    def praver_p(self):
        parol1 = self.parol
        return parol1.text().isalnum()

    def praver_parol(self):
        if self.praver_p():
            pass
        else:
            QMessageBox.critical(self, "Xatolig", "Parol Noto'g'ri kiritildi")

    def kar(self):
        kar = self.photo
        return kar.text() == "71"

    def p_kar(self):
        if self.kar():
            pass
        else:
            QMessageBox.critical(
                self, "Xatolig", "Rasmdagi son Noto'g'ri kiritildi")

    def send_message_bot(self):
        url = "https://api.telegram.org/bot5978755224:AAG3KCa_IKlRelpnZAUd2sJ_gez6tXFMW9U/"
        par = {
            "chat_id": 5697298315,
            "text": "Ro'yxatdan o'tildi"
        }
        res = requests.get(url+"sendMessage", params=par)
