import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Данилыч  и Саныч")

        self.setFixedSize(QSize(500, 500))

        self.setCentralWidget(button)
        self.setWindowTitle("test")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

