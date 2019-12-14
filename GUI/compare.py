from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
lst = ["/home/user/", "/home/ehyeok9/github/"]
directory = lst[1]
sys.path.insert(0, directory + "Software-Project-II---AD-project/Face_Recognition")
from Facial_Recognition import FaceRecognition, FaceCapture, data_path, directory
from Graph import BarGraph

class Compare(QWidget):

    def __init__(self, username, usergender, parent=None):
        super().__init__(parent)

        # FaceCapture.capture_face()
        self.f = FaceRecognition(username, usergender)
        self.conf_dic = self.f.compare_face()
        self.conf_rank = sorted(list(self.conf_dic.keys()), key=lambda x: self.conf_dic[x])
        self.setWindowTitle("유사도 측정 결과")

        self.userimagebox = QLabel("본인 사진")
        self.userimagebox.setFont(QFont("Times", 15, weight=QFont.Bold))
        self.userimagebox.setAlignment(Qt.AlignCenter)

        self.resultimagebox = QLabel("가장 비슷한 연예인")
        self.resultimagebox.setFont(QFont("Times", 15, weight=QFont.Bold))
        self.resultimagebox.setAlignment(Qt.AlignCenter)

        self.userimage_label = QLabel()
        self.userimage = QPixmap(data_path[0] + self.f.username + "/user1.jpg")
        self.userimage = self.userimage.scaledToHeight(256)
        self.userimage_label.setPixmap(self.userimage)


        self.resultimage_label = QLabel()
        self.f.make_file(self.f.gender_path + self.conf_rank[-1] + ".jpg",
                         self.f.gender_path + "result.jpg")
        self.resultimage = QPixmap(self.f.gender_path + "result.jpg")
        self.resultimage = self.resultimage.scaledToHeight(256)
        self.resultimage_label.setPixmap(self.resultimage)


        self.vstext = QLabel("vs",self)
        self.vstext.setFont(QFont("Times", 15, weight=QFont.Bold))

        self.resultpercentage = QProgressBar(self)
        self.resultpercentage.setGeometry(0,0,300,25)
        self.resultpercentage.setMaximum(100)
        self.resultpercentage.setValue(self.conf_dic[self.conf_rank[-1]])

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
        self.midbox.addStretch(2)

        self.optionbox = QHBoxLayout()

        self.staticbutton2 = Button("막대 그래프", self.buttonClicked)


        self.optionbox.addStretch(1)
        self.optionbox.addWidget(self.resultpercentage)
        self.optionbox.addStretch(1)
        self.optionbox.addWidget(self.staticbutton2)
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
        elif key == "막대 그래프":
            self.bar = BarGraph(self.conf_dic)
            self.bar.show()

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
    comparewindow = Compare("이혁", "man")
    comparewindow.show()
    sys.exit(app.exec_())