from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from button import Button
from PySide6.QtCore import Qt
from edit import Edit
from plus import PlusWidget
from dotenv import load_dotenv
import os
from delete import Delete
from edit import Edit
load_dotenv()

class StartScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stackedWidget = stacked_widget
        self.setWindowTitle("Start")

        self.plus = PlusWidget()
        self.plus.hide()
        self.plus_show = False

        self.delete = Delete()
        self.delete.hide()
        self.delete_show = False

        self.edit = Edit()
        self.edit.hide()
        self.edit_show = False

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
        self.minus_btn.clicked.connect(self.show_delete)
        self.edit_btn.clicked.connect(self.show_edit)

        screen_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        screen_layout.addLayout(bts_layout)
        tela_layout.addWidget(self.screen, alignment=Qt.AlignmentFlag.AlignCenter)

        tela_layout.addWidget(self.plus, alignment=Qt.AlignmentFlag.AlignTop)
        tela_layout.addWidget(self.delete, alignment=Qt.AlignmentFlag.AlignCenter)
        tela_layout.addWidget(self.edit, alignment=Qt.AlignmentFlag.AlignTop)
    def show_plus(self):
        if not self.plus_show:
            self.plus.show()
            self.delete.hide()
            self.edit.hide()
            self.plus_show = True
            self.delete_show = False
            self.edit_show = False
            self.plus.title_text.clear()
            self.plus.img_url.clear()
            self.plus.body_text.clear()

        else:
            self.plus.hide()
            self.plus_show = False

    def show_delete(self):
        if not self.delete_show:
            self.delete.show()
            self.plus.hide()
            self.edit.hide()
            self.delete_show = True
            self.plus_show = False
            self.edit_show = False
            self.delete.delete_text.clear()

        else:
            self.delete.hide()
            self.delete_show = False

    def show_edit(self):
        if not self.edit_show:
            self.edit.show()
            self.delete.hide()
            self.plus.hide()
            self.edit_show = True
            self.delete_show = False
            self.plus_show = False
            self.edit.edit_text.clear()
            self.edit.new_text.clear()

        else:
            self.edit.hide()
            self.edit_show = False