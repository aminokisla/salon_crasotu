import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt


class ConfirmDeleteForm(QWidget):
    def __init__(self,stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget  # Ссылка на QStackedWidget

        # Настройка окна
        self.setWindowTitle('Салон красоты')
        self.setMinimumSize(1400, 800)

        # Основной вертикальный макет
        main_layout = QVBoxLayout()
        main_layout.addStretch()  # Отступ сверху

        # Текст сообщения
        confirm_label = QLabel('Подтверждаете удаление?')
        confirm_label.setStyleSheet("font-size: 20px;")
        confirm_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(confirm_label)
        main_layout.addSpacing(20)

        # Макет для кнопок
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(40)

        # Кнопка "Да"
        yes_button = QPushButton('Да')
        yes_button.setFixedSize(100, 40)
        yes_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                border: 1px solid gray;
                border-radius: 5px;
                background-color: #E0E0E0;
            }
            QPushButton:hover {
                background-color: #C0C0C0;
            }
        """)
        yes_button.clicked.connect(self.confirm_delete)

        # Кнопка "Нет"
        no_button = QPushButton('Нет')
        no_button.setFixedSize(100, 40)
        no_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                border: 1px solid gray;
                border-radius: 5px;
                background-color: #E0E0E0;
            }
            QPushButton:hover {
                background-color: #C0C0C0;
            }
        """)
        no_button.clicked.connect(self.cancel_delete)

        # Добавляем кнопки в макет
        buttons_layout.addStretch()
        buttons_layout.addWidget(yes_button)
        buttons_layout.addWidget(no_button)
        buttons_layout.addStretch()

        # Добавляем макет с кнопками в основной макет
        main_layout.addLayout(buttons_layout)
        main_layout.addStretch()  # Отступ снизу

        # Устанавливаем основной макет
        self.setLayout(main_layout)

        # Показать окно
        self.show()

    def confirm_delete(self):
        # Логика подтверждения удаления
        self.stacked_widget.setCurrentIndex(1)  # Возвращаемся в окно клиентов

    def cancel_delete(self):
        # Возврат в окно клиентов
        self.stacked_widget.setCurrentIndex(1)
