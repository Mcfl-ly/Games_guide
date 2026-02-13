from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QDateEdit
from PySide6.QtCore import Qt

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
        layout = QVBoxLayout()
        self.setLayout(layout)

        name_data_layout = QHBoxLayout()

        title_text = QLineEdit()
        title_text.setFixedSize(450,40)
        title_text.setPlaceholderText("Titulo")

        data_text = QDateEdit()
        data_text.setFixedSize(200,40)

        body_text = QTextEdit()

        name_data_layout.addWidget(title_text, alignment=Qt.AlignmentFlag.AlignLeft)
        name_data_layout.setContentsMargins(0,10,10,15)
        # name_data_layout.addWidget(data_text, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(name_data_layout)
        name_data_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(body_text)

        body_text.setStyleSheet(style)
        title_text.setStyleSheet(style)
        data_text.setStyleSheet(style)