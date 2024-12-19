import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Салон красоты")
        self.setMinimumSize(1400, 800)

        # Стили для элементов
        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
            QLabel {
                font-size: 25px;
                font-family: Arial;
                color: black;
            }
            QLineEdit {
                border: 1px solid gray;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #0078D7;
                color: white;
                border-radius: 10px;
                font-size: 20px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QPushButton:pressed {
                background-color: #004682;
            }
        """)

        # Создание виджетов
        self.label_login = QLabel("Логин")
        self.label_login.setStyleSheet("margin-right:7px;")
        self.input_login = QLineEdit()
        self.input_login.setStyleSheet("height:35px;")
        self.label_password = QLabel("Пароль")
        self.input_password = QLineEdit()
        self.input_password.setStyleSheet("height:35px;")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.button_login = QPushButton("Войти")
        self.button_login.setStyleSheet("height:35px;"
                                        "margin-left:40px;"
                                        "width:130px;")

        self.input_login.setFixedWidth(250)
        self.input_password.setFixedWidth(250)

        # Создание layout'ов
        layout_main = QVBoxLayout()

        # Создание горизонтальных layout для логина и пароля
        layout_form_login = QHBoxLayout()
        layout_form_password = QHBoxLayout()

        # Добавление виджетов в layout'ы
        layout_form_login.addStretch()
        layout_form_login.addWidget(self.label_login, alignment=Qt.AlignmentFlag.AlignCenter)  # Текст "Логин"
        layout_form_login.addWidget(self.input_login, alignment=Qt.AlignmentFlag.AlignCenter)  # Поле ввода для логина
        layout_form_login.addStretch()

        layout_form_password.addStretch()
        layout_form_password.addWidget(self.label_password, alignment=Qt.AlignmentFlag.AlignCenter)  # Текст "Пароль"
        layout_form_password.addWidget(self.input_password,
                                       alignment=Qt.AlignmentFlag.AlignCenter)  # Поле ввода для пароля
        layout_form_password.addStretch()

        # Добавление элементов в главный вертикальный layout
        layout_main.addStretch()  # Растягиваем пространство сверху
        layout_main.addLayout(layout_form_login)  # Добавляем горизонтальный layout с логином
        layout_main.addSpacing(20)
        layout_main.addLayout(layout_form_password, )  # Добавляем горизонтальный layout с паролем
        layout_main.addSpacing(20)
        layout_main.addWidget(self.button_login, alignment=Qt.AlignmentFlag.AlignCenter)  # Кнопка
        layout_main.addStretch()  # Растягиваем пространство снизу

        # Установка основного layout
        self.setLayout(layout_main)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
