from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
sys.path.insert(0, "/home/user/Software-Project-II---AD-project/Face_Recognition")
from Facial_Recognition import FaceRecognition, FaceCapture

class Compare(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.directory_path = "/home/user/Software-Project-II---AD-project"

        FaceCapture.capture_face()
        self.f = FaceRecognition()
        self.dic = self.f.compare_face()

        self.setWindowTitle("유사도 측정 결과")

        self.userimagebox = QLabel("본인 사진")
        self.resultimagebox = QLabel("가장 비슷한 연예인")

        self.userimage_label = QLabel()
        self.userimage = QPixmap(self.directory_path + "/Face_Recognition/userFaces/user1.jpg")
        self.userimage = self.userimage.scaledToHeight(256)
        self.userimage_label.setPixmap(self.userimage)


        self.resultimage_label = QLabel()
        self.f.make_file(self.directory_path + "/Face_Recognition/othersFaces/" + self.f.conf_tuple_lst[0][0] + ".jpg",
                         self.directory_path + "/Face_Recognition/othersFaces/result.jpg")
        # self.directory_path + "/Face_Recognition/othersFaces/" + self.f.conf_tuple_lst[0][0] + ".jpg"
        self.resultimage = QPixmap(self.directory_path + "/Face_Recognition/othersFaces/result.jpg")
        self.resultimage = self.resultimage.scaledToHeight(256)
        self.resultimage_label.setPixmap(self.resultimage)


        self.vstext = QLabel("vs",self)
        self.resulttext = QLabel(str(self.f.conf_tuple_lst[0][1]) + "%", self)

        self.leftbox = QVBoxLayout()
        self.midbox = QVBoxLayout()
        self.rightbox = QVBoxLayout()

        self.leftbox.addStretch(1)
        self.leftbox.addWidget(self.userimagebox)
        self.leftbox.addStretch(1)
        self.leftbox.addWidget(self.userimage_label)
        self.leftbox.addStretch(1)


        self.rightbox.addStretch(1)
        self.rightbox.addWidget(self.resultimagebox)
        self.rightbox.addStretch(1)
        self.rightbox.addWidget(self.resultimage_label)
        self.rightbox.addStretch(1)

        self.midbox.addStretch(2)
        self.midbox.addWidget(self.vstext)
        self.midbox.addStretch(1)
        self.midbox.addWidget(self.resulttext)
        self.midbox.addStretch(1)

        self.optionbox = QHBoxLayout()
        self.staticbutton1 = Button("원그래프", self.buttonClicked)
        self.staticbutton2 = Button("막대 그래프", self.buttonClicked)
        self.staticbutton3 = Button("기타", self.buttonClicked)

        self.optionbox.addStretch(1)
        self.optionbox.addWidget(self.staticbutton1)
        self.optionbox.addStretch(1)
        self.optionbox.addWidget(self.staticbutton2)
        self.optionbox.addStretch(1)
        self.optionbox.addWidget(self.staticbutton3)
        self.optionbox.addStretch(1)

        self.mainwindow = QHBoxLayout()
        self.mainwindow.addLayout(self.leftbox)
        self.mainwindow.addLayout(self.midbox)
        self.mainwindow.addLayout(self.rightbox)

        self.realmainwindow = QVBoxLayout()
        self.realmainwindow.addLayout(self.mainwindow)
        self.realmainwindow.addLayout(self.optionbox)


        self.setLayout(self.realmainwindow)

        self.center()

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        if key == '원그래프':
            print("")
        elif key == "사용설명":
            print(123)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


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

if __name__ == '__main__':

    app = QApplication(sys.argv)
    comparewindow = Compare()
    comparewindow.show()
    sys.exit(app.exec_())

