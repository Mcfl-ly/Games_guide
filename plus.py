from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QDateEdit
from PySide6.QtCore import Qt
from button import Button
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from mongo import documento

load_dotenv()

class PlusWidget(QWidget):
    def __init__(self):
        super().__init__()
        style = """
        background-color: white;
        color: black;
        font-size: 16px;
        border: 2px solid black;
        border-radius: 5px;

        """
        #BANCO DE DADOS
        uri = os.getenv("URI")
        self.client = MongoClient(uri, server_api=ServerApi("1"))
        self.db = self.client["catalogo"]
        self.colecao = self.db["jogos"]


        layout = QVBoxLayout()
        self.setLayout(layout)

        name_data_layout = QHBoxLayout()

        self.title_text = QLineEdit()
        self.title_text.setFixedSize(350,40)
        self.title_text.setPlaceholderText("Titulo")

        self.img_url = QLineEdit()
        self.img_url.setFixedSize(300,40)
        self.img_url.setPlaceholderText("URL da imagem")

        self.body_text = QTextEdit()

        self.add_button = QPushButton("Adicionar")
        self.add_button.setStyleSheet('color: black;'
                                      f'background-color: {os.getenv('VERDE')};'
                                      'border: 2px solid black;'
                                      'font-size: 16px;'
                                      'border-radius: 5px;')
        self.add_button.setFixedSize(150,30)
        self.add_button.clicked.connect(self.add_doc)

        name_data_layout.addWidget(self.title_text, alignment=Qt.AlignmentFlag.AlignLeft)
        name_data_layout.setContentsMargins(0,10,10,15)
        name_data_layout.addWidget(self.img_url, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(name_data_layout)
        name_data_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.body_text)
        layout.addWidget(self.add_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.body_text.setStyleSheet(style)
        self.title_text.setStyleSheet(style)
        self.img_url.setStyleSheet(style)

    def add_doc(self):
        title = self.title_text.text().lower()
        img_url = self.img_url.text().lower()
        body_text = self.body_text.toPlainText().lower()
        documento = {title: title,
                     img_url: img_url,
                     body_text: body_text}
        self.colecao.insert_one(documento)