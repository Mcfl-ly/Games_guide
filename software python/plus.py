from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QDateEdit
from PySide6.QtCore import Qt
from button import Button
import os, sys, certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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


        #data e desenvolvedora
        data_dev_layout = QHBoxLayout()
        self.dev_text = QLineEdit()
        self.dev_text.setFixedSize(300, 40)
        self.dev_text.setPlaceholderText("Desenvolvedora")

        self.data_text = QLineEdit()
        self.data_text.setFixedSize(350, 40)
        self.data_text.setPlaceholderText("Lançamento")


        #titulo e url da imagem
        name_url_layout = QHBoxLayout()
        self.title_text = QLineEdit()
        self.title_text.setFixedSize(350,40)
        self.title_text.setPlaceholderText("Titulo")

        self.img_url = QLineEdit()
        self.img_url.setFixedSize(300,40)
        self.img_url.setPlaceholderText("URL da imagem")


        self.layout_steam = QHBoxLayout()

        self.steam_url = QLineEdit()
        self.steam_url.setFixedSize(400,40)
        self.steam_url.setPlaceholderText("Visite na Steam")
        self.layout_steam.addWidget(self.steam_url)

        self.add_paragrafo = QHBoxLayout()
        self.body_text = QTextEdit()
        self.add_pbutton = QPushButton("Add Paragráfo")
        self.add_pbutton.setStyleSheet("background-color: rgb(197, 247, 223);"
                                       "color: black;"
                                       "border: 2px solid black;"
                                       "font-size: 16px;"
                                       "border-radius: 5px;"
                                       "width: 100px;"
                                       "height: 50px;")
        self.add_pbutton.clicked.connect(self.adicionar_paragrafo)

        self.add_paragrafo.addWidget(self.body_text)
        self.add_paragrafo.addWidget(self.add_pbutton, alignment=Qt.AlignmentFlag.AlignBottom)

        self.add_button = QPushButton("Adicionar")
        self.add_button.setStyleSheet('color: black;'
                                      f'background-color: {os.getenv('VERDE')};'
                                      'border: 2px solid black;'
                                      'font-size: 16px;'
                                      'border-radius: 5px;')
        self.add_button.setFixedSize(150,30)
        self.add_button.clicked.connect(self.add_doc)


        data_dev_layout.addWidget(self.data_text, alignment=Qt.AlignmentFlag.AlignCenter)
        data_dev_layout.setContentsMargins(0, 10, 10, 15)
        data_dev_layout.addWidget(self.dev_text, alignment=Qt.AlignmentFlag.AlignCenter)



        name_url_layout.addWidget(self.title_text, alignment=Qt.AlignmentFlag.AlignLeft)
        name_url_layout.setContentsMargins(0,10,10,15)
        name_url_layout.addWidget(self.img_url, alignment=Qt.AlignmentFlag.AlignRight)

        #ADICIONANDO AO LAYOUT GERAL
        layout.addLayout(name_url_layout)
        layout.addLayout(data_dev_layout)
        layout.addLayout(self.layout_steam)
        layout.addLayout(self.add_paragrafo)

        name_url_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        data_dev_layout.setAlignment(Qt.AlignmentFlag.AlignRight)



        layout.addWidget(self.add_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.body_text.setStyleSheet(style)
        self.title_text.setStyleSheet(style)
        self.img_url.setStyleSheet(style)
        self.data_text.setStyleSheet(style)
        self.dev_text.setStyleSheet(style)
        self.steam_url.setStyleSheet(style)



        self.paragrafos = []

    def adicionar_paragrafo(self):
        body_text = self.body_text.toPlainText()
        self.paragrafos.append(body_text.capitalize())
        self.body_text.clear()
        print(self.paragrafos)

    def add_doc(self):
        title = self.title_text.text().capitalize()
        img_url = self.img_url.text().lower()
        body_text = self.paragrafos
        data = self.data_text.text()
        dev = self.dev_text.text().capitalize()
        link_steam = self.steam_url.text().lower()
        documento = {"titulo": title,
                     "url": img_url,
                     "texto": body_text,
                     "data": data,
                     "dev": dev,
                     "link_steam": link_steam
                     }
        self.colecao.insert_one(documento)