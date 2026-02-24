from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QHBoxLayout
from start_screen import StartScreen
from dotenv import load_dotenv
import os


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.teste = StartScreen(self.stacked_widget)

        self.setWindowTitle("Guia de jogos")
        self.setFixedSize(720, 720)
        self.setStyleSheet(f"background-color: {os.getenv("AZUL")};")

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(self.teste)


        self.stacked_widget.addWidget(container)
        self.stacked_widget.setCurrentIndex(0)
        self.show()