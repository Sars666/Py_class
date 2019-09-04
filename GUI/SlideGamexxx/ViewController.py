#界面
import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Element import Element
from ElementMatching import *
from HPBar import HPBar

class View(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        #控件生成
        self.frontFrame = QLabel()
        self.element = Element()
        self.hpBar = HPBar()


        #控件设置
        self.frontFrame.setPixmap(QPixmap('Even_Dead_Gods_Can_Die.png'))
        self.frontFrame.setScaledContents(True)
        self.frontFrame.resize(375,200)

        #布局设置
        vbox = QVBoxLayout()
        vbox.addWidget(self.frontFrame,alignment=Qt.AlignTop)
        vbox.addSpacing(50)
        vbox.addWidget(self.hpBar)
        vbox.addWidget(self.element,alignment=Qt.AlignBottom)

        self.setLayout(vbox)

        #窗口设置
        self.center()
        self.setStyleSheet("background-color:pink;")
        self.setWindowTitle('ElementMatching')
        self.show()
    '''
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        pen = QPen(Qt.black)
        brush = QBrush(QColor('black'))
        qp.setPen(pen)
        qp.setBrush(brush)
        self.frontFrame.drawFrame(qp)
        qp.drawRect(self.frontFrame.x(),self.frontFrame.y(),
                    350,100)
    '''
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    View = View()
    app.setWindowIcon(QIcon('Professors_Diploma.png'))
    sys.exit(app.exec_())