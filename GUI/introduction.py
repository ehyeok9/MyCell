from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Intro(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setWindowTitle("사용설명")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Intro()
    calc.show()
    sys.exit(app.exec_())

