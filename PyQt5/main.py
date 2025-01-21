# system specefic parameters and functions 
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(700,300,500, 500)
        self.setWindowIcon(QIcon("image.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0,500, 100)
        label.setStyleSheet("color: #292929"
                            "background-color: #6fdcf7"
                            "font-weight: bold" 
                            "font-style: italic"
                            "text-decoration: underline")

def main():
    # create the application instance
    # sys.arvgv contains command-line arguments 
    # arvgv[0]: is the script name itslef 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()