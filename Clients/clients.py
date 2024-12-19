from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, \
    QHeaderView, QStackedWidget
from Clients import confirmChanges
from Clients import editDatasClients
from Clients import addDatasClients


class ClientsWindow(QWidget):
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
        self.exit_button.clicked.connect(self.exit_to_main_menu)  # Метод переключения на главное меню

        # Добавляем кнопку справа
        top_layout.addStretch()
        top_layout.addWidget(self.exit_button)

        # Макет с таблицей и кнопками
        content_layout = QHBoxLayout()

        # Table layout
        table_layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setRowCount(14)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ФИО', 'Номер телефона'])

        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 250)
        self.table.setMaximumWidth(495)
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
        main_layout.addLayout(content_layout)  # Основное содержимое

        self.setLayout(main_layout)

        # Подключаем обработчики событий для кнопок
        self.buttons[0].clicked.connect(self.open_add_window)  # Кнопка "Добавить"
        self.buttons[1].clicked.connect(self.open_edit_window)  # Кнопка "Редактировать"
        self.buttons[2].clicked.connect(self.open_delete_window)  # Кнопка "Удалить"

        self.show()

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

    # Метод для выхода в главное меню
    def exit_to_main_menu(self):
        self.stacked_widget.setCurrentIndex(0)  # Возвращаемся в главное меню (индекс 0)

    # Обработчик для кнопки "Добавить"
    def open_add_window(self):
        # Создаем окно для добавления данных и показываем его
        add_window = addDatasClients.AddDataForm(self.stacked_widget)  # Создайте объект из вашего окна добавления данных
        self.stacked_widget.addWidget(add_window)  # Добавляем его в stacked_widget
        self.stacked_widget.setCurrentWidget(add_window)  # Переключаемся на новое окно

    # Обработчик для кнопки "Редактировать"
    def open_edit_window(self):
        # Создаем окно для редактирования данных и показываем его
        edit_window = editDatasClients.EditDataForm(self.stacked_widget)  # Создайте объект из вашего окна редактирования
        self.stacked_widget.addWidget(edit_window)  # Добавляем его в stacked_widget
        self.stacked_widget.setCurrentWidget(edit_window)  # Переключаемся на новое окно

    # Обработчик для кнопки "Удалить"
    def open_delete_window(self):
        # Создаем окно для подтверждения изменений и показываем его
        confirm_window = confirmChanges.ConfirmDeleteForm(self.stacked_widget)  # Создайте объект из вашего окна подтверждения
        self.stacked_widget.addWidget(confirm_window)  # Добавляем его в stacked_widget
        self.stacked_widget.setCurrentWidget(confirm_window)  # Переключаемся на новое окно
