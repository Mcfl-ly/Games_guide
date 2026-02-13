from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from button import Button
from PySide6.QtCore import Qt
from plus import PlusWidget
from dotenv import load_dotenv
import os

load_dotenv()

class StartScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stackedWidget = stacked_widget
        self.setWindowTitle("Start")

        self.plus = PlusWidget()
        self.plus.hide()

        tela_layout = QVBoxLayout(self)

        #WIDGET DOS BOTOES
        self.screen = QWidget()
        self.screen.setObjectName("screen")
        self.screen.setFixedSize(480, 200)
        screen_layout = QHBoxLayout(self.screen)
        screen_layout.setContentsMargins(24, 24, 24, 24)
        screen_layout.setSpacing(16)
        bts_layout = QHBoxLayout()
        self.plus_btn = Button('+', os.getenv("VERDE"))
        self.minus_btn = Button('-', os.getenv("ROSA"))
        self.edit_btn = Button('E', os.getenv("AMARELO"))
        self.src_btn = Button('SRC', os.getenv("ROXO"))
        bts_layout.addWidget(self.plus_btn)
        bts_layout.addWidget(self.minus_btn)
        bts_layout.addWidget(self.edit_btn)
        bts_layout.addWidget(self.src_btn)

        self.plus_btn.clicked.connect(self.show_plus)


        screen_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        screen_layout.addLayout(bts_layout)
        tela_layout.addWidget(self.screen, alignment=Qt.AlignmentFlag.AlignCenter)

        tela_layout.addWidget(self.plus, alignment=Qt.AlignmentFlag.AlignTop)

    def show_plus(self):
        self.plus.show()