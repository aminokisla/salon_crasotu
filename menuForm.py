import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow, QStackedWidget
from PyQt6.QtCore import Qt
from Clients.clients import ClientsWindow
from Masters.masters import MastersWindow
from Services.services import ServicesWindow
from Appointments.appointments import AppointmentsWindow
from Reports.report import ReportWindow


class MainMenuForm(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget  # Ссылка на QStackedWidget

        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.addStretch()

        # Список кнопок и функций переключения виджетов
        button_data = [
            ("Клиенты", self.show_clients),
            ("Мастера", self.show_masters),
            ("Услуги", self.show_services),
            ("Записи", self.show_appointments),
            ("Отчет", self.show_report),
        ]

        # Добавление кнопок
        self.buttons = []
        for name, handler in button_data:
            button = QPushButton(name)
            button.setFixedSize(400, 80)
            button.clicked.connect(handler)
            self.buttons.append(button)
            main_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addStretch()
        self.setLayout(main_layout)
        self.apply_button_styles()

    def apply_button_styles(self):
        """Применение стилей к кнопкам."""
        button_style = """
            QPushButton {
                background-color: #0078D7;
                color: white;
                border-radius: 10px;
                font-size: 22px;
                font-weight: bold;
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

    # Методы для переключения виджетов
    def show_clients(self):
        self.stacked_widget.setCurrentIndex(1)  # Переключаем на виджет "Клиенты"

    def show_masters(self):
        self.stacked_widget.setCurrentIndex(2)  # Переключаем на виджет "Мастера"

    def show_services(self):
        self.stacked_widget.setCurrentIndex(3)  # Переключаем на виджет "Услуги"

    def show_appointments(self):
        self.stacked_widget.setCurrentIndex(4)  # Переключаем на виджет "Записи"

    def show_report(self):
        self.stacked_widget.setCurrentIndex(5)  # Переключаем на виджет "Отчет"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Салон красоты")
        self.setMinimumSize(1400, 800)

        # QStackedWidget для хранения виджетов
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Добавляем виджеты в QStackedWidget
        self.main_menu = MainMenuForm(self.stacked_widget)
        self.clients_window = ClientsWindow(self.stacked_widget)
        self.masters_window = MastersWindow(self.stacked_widget)
        self.services_window = ServicesWindow(self.stacked_widget)
        self.appointments_window = AppointmentsWindow(self.stacked_widget)
        self.report_window = ReportWindow(self.stacked_widget)

        self.stacked_widget.addWidget(self.main_menu)         # Индекс 0
        self.stacked_widget.addWidget(self.clients_window)    # Индекс 1
        self.stacked_widget.addWidget(self.masters_window)    # Индекс 2
        self.stacked_widget.addWidget(self.services_window)   # Индекс 3
        self.stacked_widget.addWidget(self.appointments_window)  # Индекс 4
        self.stacked_widget.addWidget(self.report_window)     # Индекс 5

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
