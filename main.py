import sys
from window import Window
from PySide6.QtWidgets import QMainWindow, QApplication


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
