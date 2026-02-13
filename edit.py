from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QDateEdit
from PySide6.QtCore import Qt
from button import Button
import os
from dotenv import load_dotenv

load_dotenv()

class Edit(QWidget):
    def __init__(self):
        super().__init__()
        style = """
                background-color: white;
                color: black;
                font-size: 16px;
                border: 2px solid black;
                border-radius: 5px;

                """
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.edit_text = QLineEdit()
        self.edit_text.setStyleSheet(style)
        self.edit_text.setFixedSize(400, 40)
        self.edit_text.setPlaceholderText("Titulo")

        self.new_text = QTextEdit()
        self.new_text.setStyleSheet(style)
        self.new_text.setPlaceholderText("Novo texto")

        self.edit_btn = QPushButton("Editar")
        self.edit_btn.setStyleSheet('color: black;'
                                      f'background-color: {os.getenv('AMARELO')};'
                                      'border: 2px solid black;'
                                      'font-size: 16px;'
                                      'border-radius: 5px;')
        self.edit_btn.setFixedSize(150, 30)

        layout.addWidget(self.edit_text)
        layout.addWidget(self.new_text)
        layout.addWidget(self.edit_btn, alignment=Qt.AlignmentFlag.AlignCenter)