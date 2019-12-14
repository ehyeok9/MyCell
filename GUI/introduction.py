from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Intro(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.text = ''' 
        1. 뭐를 하신 후
        2. 뭐를 하고
        3. 이 후 뭐를 한 다음에 크흠
        4. 이혁규 존나 멋있다.
        5. 시험 슈발              
        '''

        self.mainlayout = QVBoxLayout()

        self.introduce = QTextBrowser()
        self.introduce.append(self.text)
        self.introduce.setAlignment(Qt.AlignCenter)
        self.mainlayout.addWidget(self.introduce)


        self.setWindowTitle("사용설명")
        self.setLayout(self.mainlayout)
        self.setFixedSize(640,480)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Intro()
    calc.show()
    sys.exit(app.exec_())

