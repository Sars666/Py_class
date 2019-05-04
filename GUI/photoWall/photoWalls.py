import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from glob import glob


class PhotoWall(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        names = glob('photoWallSources/*.png')
        rows = 5
        columns = 6
        vbox = QVBoxLayout()
        for row in range(rows):
            nameList = names[row*columns:(row+1)*columns]
            self.addHboxToVbox(vbox,nameList)

        self.setLayout(vbox)
        self.resize(128*columns,128*rows)#自适应尺寸
        self.setFixedSize(self.size())#固定尺寸
        self.setWindowTitle('照片墙')
        self.show()

    def addHboxToVbox(self,vbox,name):
        hbox = QHBoxLayout()
        self.hboxAddWidget(hbox,name)
        vbox.addLayout(hbox)

    def hboxAddWidget(self,hbox,names):
        for name in names:
            currentIconName = name
            icon = QLabel()
            icon.setPixmap(QPixmap(currentIconName))
            icon.setScaledContents(True)#固定图片大小
            hbox.addWidget(icon)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    photoWall = PhotoWall()
    app.setWindowIcon(QIcon('icon.png'))
    sys.exit(app.exec_())