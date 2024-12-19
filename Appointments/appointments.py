import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, \
    QHeaderView, QLabel, QComboBox
from Appointments import confirmAppointments
from Appointments import addDatasAppointments
from Appointments import editDatasAppointments

class AppointmentsWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget  # Ссылка на QStackedWidget
        self.setWindowTitle('Салон красоты')
        self.setMinimumSize(1400, 800)

        # Основной макет окна
        main_layout = QVBoxLayout()

        # Верхний макет для кнопки выхода
        top_layout = QHBoxLayout()
        self.exit_button = QPushButton("Выход в главное меню")
        self.exit_button.setMaximumWidth(200)
        self.exit_button.clicked.connect(self.exit_to_main_menu)  # Закрывает окно

        # Добавляем кнопку справа
        top_layout.addStretch()
        top_layout.addWidget(self.exit_button)

        # Добавляем новый макет для выбора мастеров
        filter_layout = QHBoxLayout()

        self.master_label = QLabel('Выберите мастера:')
        self.master_label.setFixedWidth(150)
        self.master_combobox = QComboBox()
        self.master_combobox.addItems(['Мастер 1', 'Мастер 2', 'Мастер 3', 'Мастер 4'])
        self.master_combobox.setFixedWidth(300)

        # Добавляем элементы в макет выбора мастеров
        filter_layout.addStretch()
        filter_layout.addWidget(self.master_label)
        filter_layout.addSpacing(10)
        filter_layout.addWidget(self.master_combobox)
        filter_layout.addStretch()

        # Макет с таблицей и кнопками
        content_layout = QHBoxLayout()

        # Table layout
        table_layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setRowCount(14)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Мастер', 'Дата', 'Время', 'ФИО', 'Услуга'])

        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)

        self.table.setMaximumWidth(800)
        self.table.setMaximumHeight(400)

        # Fix column resizing
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        # Fix row resizing
        vertical_header = self.table.verticalHeader()
        vertical_header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        # Prevent editing the table content
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        table_layout.addWidget(self.table)
        content_layout.addLayout(table_layout)

        # Buttons layout
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(20)  # Пространство между кнопками
        buttons_layout.addStretch()

        # Создаем массив кнопок
        button_names = ['Добавить', 'Редактировать', 'Удалить']
        self.buttons = []  # Список для хранения кнопок

        for name in button_names:
            button = QPushButton(name)
            button.setMaximumWidth(300)

            # Добавляем кнопку в массив и в макет
            self.buttons.append(button)
            buttons_layout.addWidget(button)

        buttons_layout.addStretch()

        # Применяем стили к кнопкам
        self.apply_button_styles()

        content_layout.addLayout(buttons_layout)

        # Добавляем все макеты в основной макет
        main_layout.addLayout(top_layout)  # Верхний макет с кнопкой выхода
        main_layout.addLayout(filter_layout)  # Макет для выбора мастера
        main_layout.addLayout(content_layout)  # Основное содержимое

        self.setLayout(main_layout)

        self.buttons[0].clicked.connect(self.open_add_window)  # Кнопка "Добавить"
        self.buttons[1].clicked.connect(self.open_edit_window)  # Кнопка "Редактировать"
        self.buttons[2].clicked.connect(self.open_delete_window)  # Кнопка "Удалить"

        self.show()
    # Метод для выхода в главное меню
    def exit_to_main_menu(self):
        self.stacked_widget.setCurrentIndex(0)  # Возвращаемся в главное меню (индекс 0)

    def open_add_window(self):
        # Создаем окно для добавления данных и показываем его
        add_window = addDatasAppointments.AddDataForm(self.stacked_widget)  # Создайте объект из вашего окна добавления данных
        self.stacked_widget.addWidget(add_window)  # Добавляем его в stacked_widget
        self.stacked_widget.setCurrentWidget(add_window)  # Переключаемся на новое окно

    # Обработчик для кнопки "Редактировать"
    def open_edit_window(self):
        # Создаем окно для редактирования данных и показываем его
        edit_window = editDatasAppointments.EditDataForm(self.stacked_widget)  # Создайте объект из вашего окна редактирования
        self.stacked_widget.addWidget(edit_window)  # Добавляем его в stacked_widget
        self.stacked_widget.setCurrentWidget(edit_window)  # Переключаемся на новое окно

    # Обработчик для кнопки "Удалить"
    def open_delete_window(self):
        # Создаем окно для подтверждения изменений и показываем его
        confirm_window = confirmAppointments.ConfirmDeleteForm(self.stacked_widget)  # Создайте объект из вашего окна подтверждения
        self.stacked_widget.addWidget(confirm_window)  # Добавляем его в stacked_widget
        self.stacked_widget.setCurrentWidget(confirm_window)  # Переключаемся на новое окно

    def apply_button_styles(self):
        button_style = """
            QPushButton {
                background-color: #0078D7;
                color: white;
                border-radius: 10px;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QPushButton:pressed {
                background-color: #004682;
            }
        """
        for button in self.buttons:
            button.setStyleSheet(button_style)

        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #D9534F;
                color: white;
                border-radius: 10px;
                font-size: 14px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #C9302C;
            }
            QPushButton:pressed {
                background-color: #AC2925;
            }
        """)
