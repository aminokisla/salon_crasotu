import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt


class EditDataForm(QWidget):
    def __init__(self,stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget  # Ссылка на QStackedWidget

        # Настройка окна
        self.setWindowTitle('Салон красоты')
        self.setMinimumSize(1400, 800)

        # Основной вертикальный макет
        main_layout = QVBoxLayout()
        main_layout.addStretch()  # Отступ сверху

        # Заголовок формы
        title_label = QLabel('Редактирование данных')
        title_label.setStyleSheet("font-size: 25px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)
        main_layout.addSpacing(40)

        # Список меток и полей ввода
        labels = ['Услуга', 'Мастер', 'Дата', 'Время']
        self.inputs = []  # Список для хранения QLineEdit

        # Макет для формы
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)

        # Создаем строки с QHBoxLayout для каждой пары (QLabel + QLineEdit)
        for i, label_text in enumerate(labels, start=1):
            row_layout = QHBoxLayout()

            # QLabel - текст слева
            label = QLabel(label_text)
            label.setFixedWidth(150)  # Фиксированная ширина метки
            label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

            # QLineEdit - поле ввода справа
            input_field = QLineEdit()
            input_field.setFixedWidth(300)  # Фиксированная ширина поля ввода

            # Добавляем в строку
            row_layout.addStretch()
            row_layout.addWidget(label)
            row_layout.addSpacing(10)
            row_layout.addWidget(input_field)
            row_layout.addStretch()

            # Добавляем строку в макет формы
            form_layout.addLayout(row_layout)
            self.inputs.append(input_field)  # Сохраняем поле ввода

        # Добавляем форму в основной макет
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(40)


        # Кнопка "Сохранить"
        save_button = QPushButton('Сохранить')
        save_button.setFixedSize(220, 60)
        save_button.clicked.connect(self.save_and_return)

        save_button.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                border-radius: 10px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
        """)

        # Макет для кнопки
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(save_button)
        button_layout.addStretch()

        # Добавляем кнопку в основной макет
        main_layout.addLayout(button_layout)
        main_layout.addStretch()  # Отступ снизу

        # Устанавливаем основной макет окна
        self.setLayout(main_layout)

        self.setStyleSheet("""
        QLineEdit {
            border: 1px solid gray;
            border-radius: 5px;
            padding: 5px;
            font-size: 14px;
            height:50px;
            }
        QLabel{
            font-size:20px;
        }
            """)

        # Показать окно
        self.show()
    def save_and_return(self):
        """Сохранить данные и вернуться в окно клиентов."""
        # Логика сохранения данных может быть добавлена здесь
        self.stacked_widget.setCurrentIndex(1)  # Возвращаемся в ClientsWindow