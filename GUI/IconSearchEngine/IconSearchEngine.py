import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from glob import glob


class SearchResult(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #搜索结果
        names = glob('SearchResult/*.png')
        rows = 4
        columns = 5
        grid = QGridLayout()

        self.setLayout(grid)

        positions = [(c,r) for c in range(columns)
                     for r in range(rows)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.show()

class SearchEngineUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #控件定义
        searchBtn = QPushButton(self)
        nextPageBtn = QPushButton(self)
        lastPageBtn = QPushButton(self)
        iconLabel = QLabel(self)
        keyWordEdit = QLineEdit(self)

        searchResult = SearchResult()
        self.setCentralWidget(searchResult)


        #位置设置
        keyWordEdit.move(50,100)
        iconLabel.move(290,30)
        searchBtn.move(500,95)
        nextPageBtn.move(315,650)
        lastPageBtn.move(235,650)

        searchResult.move(100,100)

        #大小设置
        keyWordEdit.resize(450,50)
        iconLabel.resize(50,50)
        iconLabel.setScaledContents(True)
        searchBtn.resize(100,60)
        nextPageBtn.resize(80,50)
        lastPageBtn.resize(80,50)

        #控件内容设置
        iconLabel.setPixmap(QPixmap('icon.png'))
        searchBtn.setText('搜索')
        nextPageBtn.setText('下一页')
        lastPageBtn.setText('上一页')


        #窗口设置
        self.resize(640,712)#自适应尺寸
        # self.setFixedSize(self.size())#固定尺寸
        self.setWindowTitle('iconSearchEngine')
        self.show()

    def search(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    SearchEngine = SearchEngineUI()
    # SearchResult = SearchResult()
    app.setWindowIcon(QIcon('icon.png'))    #设置图标
    sys.exit(app.exec_())