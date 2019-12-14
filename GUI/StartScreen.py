from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from compare import Compare
from introduction import Intro
from regist import Register, user_lst
import os
import sys
import pickle
lst = ["/home/user/", "/home/ehyeok9/github/"]
directory = lst[0]
sys.path.insert(0, directory + "Software-Project-II---AD-project/Face_Recognition")
from Facial_Recognition import data_path

class ComboBox(QComboBox):
    popupAboutToBeShown = pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()

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

        self.textinput = QLineEdit()
        self.removebutton = Button("유저삭제", self.buttonClicked)
        self.enrollmentbutton = Button("등록하기", self.buttonClicked)
        self.startbutton = Button("결과보기", self.buttonClicked)
        self.introductionbutton = Button("사용설명", self.buttonClicked)

        self.combobox = ComboBox(self)
        self.combobox.popupAboutToBeShown.connect(self.updateComb)

        self.hlayout = QHBoxLayout(self)
        self.vlayout = QVBoxLayout(self)
        self.buttonLayout = QVBoxLayout(self)

        self.removelayout = QHBoxLayout()
        self.removelayout.addWidget(self.textinput)
        self.removelayout.addWidget(self.removebutton)

        self.buttonLayout.addLayout(self.removelayout)
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
            username = self.combobox.currentText()
            usergender = None
            for user in user_lst:
                if user["name"] == username:
                    usergender = user["gender"]
            self.exec = Compare(username, usergender)
            self.exec.show()
        elif key == "사용설명":
            self.intro = Intro()
            self.intro.show()
        elif key == "등록하기":
            self.register = Register()
            self.register.show()
        elif key == "유저삭제":
            username = self.textinput.text()
            for i, user in enumerate(user_lst):
                if user["name"] == username:
                    os.system("rm -r {}".format(data_path[0] + username + '/'))
                    del user_lst[i]
                    with open('user_info.txt', 'wb') as f:
                        pickle.dump(user_lst, f)

        

    def updateComb(self):
        self.combobox.clear()
        for user in user_lst:
            self.combobox.addItem(user["name"])

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

