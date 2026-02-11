from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from button import Button
from PySide6.QtCore import Qt
class StartScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stackedWidget = stacked_widget
        self.setWindowTitle("Start")

        tela_layout = QVBoxLayout(self)

        #WIDGET DOS BOTOES
        self.screen = QWidget()
        self.screen.setObjectName("screen")
        self.screen.setFixedSize(480, 1000)
        screen_layout = QHBoxLayout(self.screen)
        screen_layout.setContentsMargins(24, 24, 24, 24)
        screen_layout.setSpacing(16)
        bts_layout = QHBoxLayout()
        self.plus_btn = Button('+', 'green')
        self.minus_btn = Button('-', 'red')
        self.edit_btn = Button('E', 'blue')
        self.src_btn = Button('SRC', 'purple')
        bts_layout.addWidget(self.plus_btn)
        bts_layout.addWidget(self.minus_btn)
        bts_layout.addWidget(self.edit_btn)
        bts_layout.addWidget(self.src_btn)

        screen_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        screen_layout.addLayout(bts_layout)
        tela_layout.addWidget(self.screen, alignment=Qt.AlignmentFlag.AlignCenter)
