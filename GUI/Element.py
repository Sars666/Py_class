#游戏操作的元素块
import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Element(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        pixmap = QPixmap("fire.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)


        self.move(300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Element()
    sys.exit(app.exec_())