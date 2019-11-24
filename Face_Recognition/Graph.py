import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
sys.path.insert(0, "/home/user/Software-Project-II---AD-project/Face_Recognition")
from Facial_Recognition import FaceRecognition
import numpy as np
import matplotlib

class BarGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")
        self.setWindowIcon(QIcon('icon.png'))

        self.lineEdit = QLineEdit()
        self.pushButton = QPushButton("차트그리기")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addStretch(1)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        f = FaceRecognition()
        dic = f.compare_face()

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

        # plt.xlim(-1, n_groups)
        # plt.ylim(min(y1_value) - 1, max(y1_value) + 1)

        # code = self.lineEdit.text()

        self.canvas.draw()
