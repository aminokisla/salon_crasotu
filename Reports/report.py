import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,
    QTextEdit, QComboBox, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSizePolicy
import random


class ReportWindow(QWidget):
    def __init__(self,stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget  # Ссылка на QStackedWidget

        # Настройки окна
        self.setWindowTitle('Салон красоты')
        self.setMinimumSize(1400, 800)

        # Основной горизонтальный макет
        main_layout = QHBoxLayout()

        # Левая часть с отчетом
        left_layout = QVBoxLayout()

        # Поле для отображения отчета (3)
        self.report_field = QTextEdit()
        self.report_field.setPlaceholderText("Отчет отобразится здесь...")
        self.report_field.setReadOnly(True)
        self.report_field.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.report_field.setStyleSheet("font-size: 20px; padding: 10px;")
        self.report_field.setMaximumWidth(600)
        left_layout.addWidget(self.report_field)

        main_layout.addLayout(left_layout)

        # Правая часть с кнопками и выбором
        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.exit_button = QPushButton("Выйти в главное меню")
        self.exit_button.setMaximumWidth(200)
        self.exit_button.clicked.connect(self.exit_to_main_menu)
        self.exit_button.setStyleSheet("""
                   QPushButton {
                       background-color: #D9534F;
                       color: white;
                       border-radius: 10px;
                       font-size: 20px;
                       padding: 15px;
                   }
                   QPushButton:hover {
                       background-color: #C9302C;
                   }
                   QPushButton:pressed {
                       background-color: #AC2925;
                   }
               """)
        self.exit_button.setMaximumWidth(300)
        self.exit_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.exit_button)
        right_layout.addLayout(button_layout)

        # Поле для выбора промежутка времени (2)
        self.time_label = QLabel("Выберите промежуток времени:")
        self.time_label.setStyleSheet("font-size: 20px;")
        self.time_combo_box = QComboBox()
        self.time_combo_box.addItems([
            "Сегодня", "Вчера", "Прошлая неделя", "Прошлый месяц", "Этот год"
        ])
        self.time_combo_box.setStyleSheet("font-size: 18px; padding: 5px;")
        self.time_combo_box.setMaximumWidth(300)
        self.time_combo_box.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        right_layout.addSpacing(300)
        right_layout.addWidget(self.time_label)
        right_layout.addWidget(self.time_combo_box)

        # Кнопка "Рассчитать"
        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.setMaximumWidth(300)
        self.calculate_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        right_layout.addSpacing(20)
        right_layout.addWidget(self.calculate_button)

        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

        self.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                border-radius: 10px;
                font-size: 20px;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QPushButton:pressed {
                background-color: #004682;
            }
        """)
    def exit_to_main_menu(self):
        self.stacked_widget.setCurrentIndex(0)  # Возвращаемся в главное меню (индекс 0)
