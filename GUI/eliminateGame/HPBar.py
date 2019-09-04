#游戏操作的元素块
import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class HPBar(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        hpBarIcon = QLabel()
        hpBar = QLabel()

        hpBar.setText('1000000/100000')
        hpBar.resize(30,100)
        hpBarIcon.resize(50,50)
        hpBarIcon.setScaledContents(False)
        hpBarIcon.setPixmap(QPixmap('Heart.png'))


        hbox.addWidget(hpBarIcon,stretch=1,alignment=Qt.AlignLeft)
        hbox.addWidget(hpBar,stretch=1,alignment=Qt.AlignRight)
        self.setLayout(hbox)
        self.resize(516,30)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HPBar()
    sys.exit(app.exec_())