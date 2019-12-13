from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from compare import Compare
from introduction import Intro

lst = ["/home/user/", "/home/ehyeok9/github/"]
directory = lst[0]

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 10)
        size.setWidth(max(size.width(), size.height()))
        return size



class FaceRecognition(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # 윈도우 타이틀
        self.setWindowTitle("Face Recognition")

        # 배경화면
        # 이미지 가져오기
        self.background = QImage(directory + "Software-Project-II---AD-project/GUI/background.jpg")
        self.background = self.background.scaled(QSize(1500,860))
        # 이미지를 넣기 위한 파레뜨 생성
        self.palette = QPalette()
        self.palette.setBrush(10, QBrush(self.background))


        # 시작화면 레이아웃
        self.title = QLabel("Face Recognition")
        self.title.setStyleSheet("color:#3232FF")
        self.title.setFont(QFont("Times", 50, weight= QFont.Bold))

        self.enrollmentbutton = Button("등록갱", self.buttonClicked)
        self.startbutton = Button("결과보기", self.buttonClicked)
        self.introductionbutton = Button("사용설명", self.buttonClicked)
        self.combobox = QComboBox(self)

        self.hlayout = QHBoxLayout(self)
        self.vlayout = QVBoxLayout(self)
        self.buttonLayout = QVBoxLayout(self)

        self.buttonLayout.addWidget(self.enrollmentbutton)

        self.vlayout.addWidget(self.title)
        self.vlayout.addStretch(2)

        self.resultlayout = QHBoxLayout(self)
        self.resultlayout.addWidget(self.combobox)
        self.resultlayout.addWidget(self.startbutton)

        self.buttonLayout.addLayout(self.resultlayout)

        self.buttonLayout.addStretch(3)
        self.buttonLayout.addWidget(self.introductionbutton)

        self.vlayout.addLayout(self.buttonLayout)
        self.vlayout.addStretch(1)

        self.hlayout.addStretch(1)
        self.hlayout.addLayout(self.vlayout)

        self.setPalette(self.palette)

        # 윈도우 크기 고정
        self.setFixedSize(1500, 860)

        self.center()

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        if key == '결과보기':
            self.exec = Compare()
            self.exec.show()
        elif key == "사용설명":
            self.intro = Intro()
            self.intro.show()
        elif key == "등록갱":
            print("afsaf")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    fr = FaceRecognition()
    fr.show()
    sys.exit(app.exec_())

