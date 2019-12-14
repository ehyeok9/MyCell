from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Intro(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.text = ''' 
        1. 등록 버튼을 누르고 새로운 창이 뜨면 사용자의 이름과 성별을 입력하고 확인 버튼을 누르면 등록이 완료된다.
        2. 등록이 완료되었다면 창을 닫는다.
        2. 등록이 성공적으로 되었다면 결과 보기 버튼 바로 왼쪽에 있는 항목을 열어 자신이 등록했던 이름을 선택한다.
        3. 항목을 닫았을 때 등록했던 이름이 올라와 있는 것이 확인되면 결과 보기 버튼을 누른다.
        4. 결과 보기 버튼을 누르면 자신의 얼굴과 데이터터베이스에 저장된 얼굴 중에서 가장 비슷한 얼굴을 골라 보여준다.
        5. 결과 창에서 상위 top 10의 통계를 보고 싶다면 막대그래프 버튼을 누르면 된다.
        6. 막대 그래프 창에 들어가면 통계가 바로 뜨지 않는데 이 때 Draw 버튼을 누르면 그래프를 그려준다.
        7. Draw 버튼을 다시 누르면 색깔이 변한다. 누를 때마다 색깔이 변한다.
        8. 만약 데이터베이스에 저장된 모든 얼굴과의 대조 결과를 얻고 싶다면 More 버튼을 누르면 된다.
        9. 결과 보기를 종료하고 싶다면 최근에 떴던 창을 순서대로 종료하면 된다.
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

