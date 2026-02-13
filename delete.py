from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QDateEdit
from PySide6.QtCore import Qt
from button import Button
import os
from dotenv import load_dotenv

load_dotenv()

class Delete(QWidget):
    def __init__(self):
        super().__init__()

        style = """
                background-color: white;
                color: black;
                font-size: 16px;
                border: 2px solid black;
                border-radius: 5px;
                """

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.del_btn = QPushButton("Excluir jogo")
        self.del_btn.setStyleSheet(F"background-color: {os.getenv("ROSA")};"
                "color: black;"
                "font-size: 16px;"
                "border: 2px solid black;"
                "border-radius: 5px;")
        self.del_btn.setFixedSize(100,40)

        self.delete_text = QLineEdit()
        self.delete_text.setStyleSheet(style)
        self.delete_text.setFixedSize(400,40)
        self.delete_text.setPlaceholderText("Titulo")
        layout.addWidget(self.delete_text)
        layout.addWidget(self.del_btn)
