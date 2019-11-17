from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Compare(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        types1 = QLabel('Label', self)
        types1.resize(170, 20)
        types1.move(1470, 580)

        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle("Directory Viewer")
        self.tree.resize(323, 300)
        self.tree.show()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Compare()
    #calc.show()
    sys.exit(app.exec_())

