import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()
        self.setGeometry(700,300,500,500)

        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        # label.setGeometry(0,0,500, 500)
        pixmap = QPixmap("image.png")
        label.setPixmap(pixmap)
        # if you run it till this you will notice that the image does not scale to the size of the object 
        # to enable that: 
        label.setScaledContents(True) #now are image will scale to the size of the label 

        label.setGeometry(
            (self.width() - label.width()) // 2,  # Center horizontally
            (self.height() - label.height()) // 2,  # Center vertically
            label.width(),  # Set the width of the label
            label.height()  # Set the height of the label
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main( )