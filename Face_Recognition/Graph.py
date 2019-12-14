import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Facial_Recognition import FaceRecognition
import numpy as np
import matplotlib

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setText(text)
        self.clicked.connect(callback)

class BarGraph(QWidget):
    def __init__(self, dic):
        super().__init__()
        self.conf_dict = dic
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("viewer")
        self.setWindowIcon(QIcon('icon.png'))

        self.lineEdit = QLineEdit()
        self.drawButton = Button("Draw", self.pushButtonClicked)
        self.moreButton = Button("More", self.pushButtonClicked)
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.drawButton)
        rightLayout.addWidget(self.moreButton)
        rightLayout.addWidget(self.textEdit)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        button = self.sender()
        key = button.text()
        dic = self.conf_dict
        print(self.conf_dict)

        if key == "Draw":
            # f = FaceRecognition()
            # dic = f.compare_face()

            if len(dic) > 10:
                conf_rank = sorted(list(self.conf_dict.keys()), key=lambda x: self.conf_dict[x], reverse=True)
                dic = {x: dic[x] for x in conf_rank[:10]}

            y1_value = list(dic.values())
            x_name = list(dic.keys())
            n_groups = len(x_name)
            index = np.arange(n_groups)

            matplotlib.rc('font', family='NanumGothic')
            ax = self.fig.add_subplot(111)

            ax.bar(index, y1_value, tick_label=x_name, align='center')
            ax.set_xlabel('Name')
            ax.set_ylabel('Confidence (%)')
            ax.set_title('Chart')

            ax.set_xlim(-1, n_groups)
            ax.set_ylim(min(y1_value) - 1, max(y1_value) + 1)

            self.canvas.draw()

        elif key == "More":
            displayString = ""
            for i in sorted(list(self.conf_dict.keys()), key=lambda x: self.conf_dict[x], reverse=True):
                if i == "result":
                    continue
                displayString += "{} = {} ".format(i, dic[i])
                displayString += "\n"

            self.textEdit.setText(displayString)
            self.textEdit.setFontPointSize(30)

        # code = self.lineEdit.text()
