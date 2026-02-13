from PySide6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, text, color):
        super().__init__()
        style = f"""
        background-color: {color};
        font-size: 40px;
        color: black;
        border: 2px solid black;
        border-radius: 10px;

        """
        self.setStyleSheet(style)
        self.setText(text)
        self.setFixedSize(100,100)