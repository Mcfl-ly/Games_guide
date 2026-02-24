from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QDateEdit
from PySide6.QtCore import Qt
from button import Button
import os, sys, certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

        # BANCO DE DADOS
        uri = os.getenv("URI")
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return None  # se não estiver empacotado, retorna None

        ca_file = resource_path("certifi/cacert.pem") or certifi.where()

        self.client = MongoClient(uri, server_api=ServerApi("1"), tlsCAFile=ca_file)
        self.db = self.client["catalogo"]
        self.colecao = self.db["jogos"]

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
        self.edit_btn.clicked.connect(self.edit_doc)

        layout.addWidget(self.edit_text)
        layout.addWidget(self.new_text)
        layout.addWidget(self.edit_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def edit_doc(self):
        title = self.edit_text.text().lower()
        text = self.new_text.toPlainText()

        filtro = {"titulo": title}
        new_value = {"$set": {"texto": text}}
        self.colecao.update_one(filtro, new_value)