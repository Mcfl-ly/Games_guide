from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QDateEdit
from PySide6.QtCore import Qt
from button import Button
import os, sys, certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


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


        layout = QHBoxLayout()
        self.setLayout(layout)

        self.del_btn = QPushButton("Excluir jogo")
        self.del_btn.setStyleSheet(F"background-color: {os.getenv("ROSA")};"
                "color: black;"
                "font-size: 16px;"
                "border: 2px solid black;"
                "border-radius: 5px;")
        self.del_btn.setFixedSize(100,40)
        self.del_btn.clicked.connect(self.del_doc)

        self.delete_text = QLineEdit()
        self.delete_text.setStyleSheet(style)
        self.delete_text.setFixedSize(400,40)
        self.delete_text.setPlaceholderText("Titulo")
        layout.addWidget(self.delete_text)
        layout.addWidget(self.del_btn)

    def del_doc(self):
        title = self.delete_text.text().lower()

        documento = {"titulo": title}
        self.colecao.delete_one(documento)
