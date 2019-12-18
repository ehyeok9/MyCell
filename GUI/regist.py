from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import pickle
lst = ["/home/user/", "/home/ehyeok9/github/"]
directory = lst[0]
sys.path.insert(0, directory + "Software-Project-II---AD-project/Face_Recognition")
from Facial_Recognition import FaceRecognition, FaceCapture, data_path, directory
try:
    with open('user_info.txt', 'rb') as f:
        user_lst = pickle.load(f)
except:
    user_lst = []

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Register(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # 윈도우 타이틀
        self.setWindowTitle("Register")

        # 배경화면
        # 이미지 가져오기
        self.search = QLineEdit()

        self.userimage_label = QLabel()
        self.userimage = QPixmap(directory + "Software-Project-II---AD-project/Face_Recognition/gray.jpg")
        self.userimage = self.userimage.scaledToHeight(256)
        self.userimage_label.setPixmap(self.userimage)
        # 이미지를 넣기 위한 파레뜨 생성

        # 시작화면 레이아웃
        self.title = QLabel("Face Recognition")
        self.title.setStyleSheet("color:#3232FF")
        self.title.setFont(QFont("Times", 50, weight= QFont.Bold))

        self.namelabel = QLabel("Name")

        self.progress = QProgressBar()
        self.progress.setGeometry(0,0,500, 25)
        self.progress.setMaximum(100)

        self.combo = QComboBox(self)
        self.combo.addItem("man")
        self.combo.addItem("woman")

        self.searchbutton = Button("검색", self.buttonClicked)

        self.mainlayout = QHBoxLayout()
        self.rightlayout = QVBoxLayout()

        self.rightlayout.addStretch(1)
        self.rightlayout.addWidget(self.namelabel)
        self.rightlayout.addWidget(self.search)
        self.rightlayout.addStretch(1)
        self.rightlayout.addWidget(self.combo)
        self.rightlayout.addStretch(1)
        self.rightlayout.addWidget(self.searchbutton)
        self.rightlayout.addStretch(4)
        self.rightlayout.addWidget(self.progress)
        self.rightlayout.addStretch(2)

        self.mainlayout.addWidget(self.userimage_label)
        self.mainlayout.addLayout(self.rightlayout)
        # # 윈도우 크기 고정
        # self.setFixedSize(800, 600)
        self.setLayout(self.mainlayout)
        self.center()

    def buttonClicked(self):
        global user_lst

        combotext = self.combo.currentText()
        searchtext = self.search.text()

        dic = {"name": searchtext, "gender": combotext}
        user_lst.append(dic)
        FaceCapture.capture_face(searchtext)

        with open('user_info.txt', 'wb') as f:
            pickle.dump(user_lst, f)

        self.userimage = QPixmap(directory + "Software-Project-II---AD-project/Face_Recognition/userFaces/" + searchtext + "/user1.jpg")
        self.userimage = self.userimage.scaledToHeight(256)
        self.userimage_label.setPixmap(self.userimage)
        self.setLayout(self.mainlayout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    fr = Register()
    fr.show()
    sys.exit(app.exec_())
