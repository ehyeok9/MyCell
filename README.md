Software Project II
===================

소프트웨어 프로젝트2 과목의 Adventure Design을 위한 보고서입니다.

주제 : **얼굴 인식을 통한 유사도 측정**

요구사항 수집, 분석
-------------------

> 얼굴 인식을 이용해서 연예인과의 얼굴 유사도를 분석하고 표로 나타내보자.

1.	노트북에 내장된 전면카메라를 이용해 사진을 찍어 자신의 얼굴의 학습데이터를 만든다.
2.	학습된 데이터를 바탕으로 얼굴 인식 AI를 만든다.
3.	AI가 DB에 저장된 연예인 사진들을 얼굴 인식 AI에 입력으로 하여 어느정도 유사도가 나오는지 계산하고 저장한다.
4.	저장한 데이터를 python의 matplotlib를 통해 그래프를 그린다.
5.	python의 pyqt가 제공하는 GUI를 통해 만들어진 그래프를 표시한다.
6.	클릭 시 추가적인 정보(비교에 사용된 연예인 사진)를 확인할 수 있는 기능 구현
7.	자신이 가지고 있는 사진도 등록해서 그 사람과의 유사도를 측정할 수 있는 기능 구현.

소프트웨어 구조 설계
--------------------

이미지 가공 알고리즘(차용), 학습 알고리즘(차용), DB(AI 데이터, 연예인 사진 저장, 분석 결과 저장), matplotlib를 이용한 그래프 구현 알고리즘, pyqt GUI 코드 파일 통합, 유저 친화적인 인터페이스 개발

<table class="tg">
  <tr>
    <th class="tg-baqh">모듈</th>
    <th class="tg-baqh">클래스</th>
    <th class="tg-baqh">역할</th>
  </tr>
  <tr>
    <td class="tg-j844" rowspan="2">Facial_Recognition.py</td>
    <td class="tg-9wq8">FaceRecognition</td>
    <td class="tg-0pky">유저의 얼굴을 바탕으로 머신러닝 학습을 하고 학습된 AI를 이용해 유저의 얼굴과 연예인 얼굴을 비교해 유사율을 측정한다.</td>
  </tr>
  <tr>
    <td class="tg-9wq8">FaceCapture</td>
    <td class="tg-0pky">기본 값으로 지정되어 있는 카메라를 통해 얼굴 사진을 찍고 유저마다 유저의 사진을 저장하는 폴더를 만든다.</td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="2">Graph.py</td>
    <td class="tg-9wq8">Button</td>
    <td class="tg-0pky">버튼의 생성과 이벤트 메소드와의 연결을 한 번에 해준다.</td>
  </tr>
  <tr>
    <td class="tg-9wq8">BarGraph</td>
    <td class="tg-0pky">유저와 연예인과의 얼굴 유사도가 저장되어 있는 딕셔너리를 받고 상위 10개를 뽑아 matplotlib를 통해 그래프를 그린다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">compare.py</td>
    <td class="tg-nrix">Compare</td>
    <td class="tg-0lax">유사도 딕셔너리 안에서 가장 유사도가 높은 사진과 유저의 사진을 출력하는 결과창. 그래프를 볼 수 있는 버튼이 포함되어 있다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">introduction.py</td>
    <td class="tg-nrix">Intro</td>
    <td class="tg-0lax">기본적인 사용설명을 적어 놓은 창.</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="2">regist.py</td>
    <td class="tg-nrix">Button</td>
    <td class="tg-0lax">버튼의 생성과 이벤트 메소드와의 연결을 한 번에 해준다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">Register</td>
    <td class="tg-0lax">유저의 사진을 등록하는 기능을 가지고 있는 창.</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="3">StartScreen.py</td>
    <td class="tg-nrix">ComboBox</td>
    <td class="tg-0lax">콤보 박스를 클릭할 때마다 자동으로 값을 업데이트 해주기 위해서 사전에 필요한 클래스.</td>
  </tr>
  <tr>
    <td class="tg-nrix">Button</td>
    <td class="tg-0lax">버튼의 생성과 이벤트 메소드와의 연결을 한 번에 해준다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">MainWindow</td>
    <td class="tg-0lax">유저 삭제 버튼, 유저 등록 버튼, 사용 설명 버튼, 결과 보기 버튼 등을 갖춘 메인 창.</td>
  </tr>
</table>

클래스 인터페이스 설계
-------------------------------

<table class="tg">
  <tr>
    <th class="tg-baqh">클래스</th>
    <th class="tg-baqh">메소드</th>
    <th class="tg-baqh">입력인자</th>
    <th class="tg-baqh">출력인자</th>
    <th class="tg-baqh">기능</th>
  </tr>
  <tr>
    <td class="tg-j844" rowspan="5">FaceRecognition</td>
    <td class="tg-9wq8">__init__</td>
    <td class="tg-c3ow">self, username, usergender</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">유저의 정보를 인자로 받아와 성별에 따라 다른 비교 데이터가 저장되어있는 디렉토리의 위치를 받아온다.  또한 이름과 일치하는 디렉토리에서 사진을 받아와 학습을 진행한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">face_detector</td>
    <td class="tg-baqh">self, img</td>
    <td class="tg-baqh">img, roi</td>
    <td class="tg-0lax">이미지를 받아와 얼굴 부분을 잘라낸 다음 200 x 200 크기로 맞춰 roi와 원본이미지를 출력한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">compare_face</td>
    <td class="tg-baqh">self </td>
    <td class="tg-baqh">conf_dict</td>
    <td class="tg-0lax">유저의 얼굴과 유저의 성별에 맞는 연예인의 얼굴을 비교해 key는 연예인의 이름 value는 유사도로 해서 딕셔너리로 묶은 다음 출력한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">draw_graph</td>
    <td class="tg-baqh">self, table</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">인자로 딕셔너리를 받아와 matplotlib를 이용해 그래프를 그린다. 주어진 파일 안에서 테스트하기 위해서 만들어진 함수이다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">make_file</td>
    <td class="tg-baqh">self, filepath, revised_filepath</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">유저와 가장 유사도가 높게 나온 사진을 보여줄 때 전신 사진이 아니라 얼굴 사진만을 보여주기 위해서 이미지를 가공해서 새로 이미지를 만드는 기능을 구현했다.</td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="2">FaceCapture</td>
    <td class="tg-9wq8">face_extractor</td>
    <td class="tg-c3ow">img</td>
    <td class="tg-baqh">cropped_face</td>
    <td class="tg-0lax">기능은 크게 face_detector와 다르지 않으나 capture_face를 스태틱 메소드로 사용하고 싶어서 추가한 기능이다. 출력이 face_detector와 다르게 cropped_face 하나 밖에 없다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">capture_face</td>
    <td class="tg-baqh">username</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">기본 설정된 카메라를 통해 사진을 찍는다. 사진을 찍고 얼굴이라고 인지된 사진을 100장 뽑아 낼 때까지 루프를 돈다. 유저 이름을 인자로 받아와 유저이름을 갖는 디렉토리를 생성하고 그 안에 얼굴사진 100장을 저장한다.</td>
  </tr>
  <tr>
    <td class="tg-9wq8">Button</td>
    <td class="tg-9wq8">__init__</td>
    <td class="tg-c3ow">self, text, callback</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">텍스트의 이름을 갖는 버튼을 만들고 callback 함수 인자에 주어진 함수로 이벤트 메소드를 연결한다.</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="3">BarGrapth</td>
    <td class="tg-baqh">__init__</td>
    <td class="tg-baqh">self, dic</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">유사도가 기록된 딕셔너리를 받아 self.conf_dict에 저장하고 setupUI를 호출한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">setupUI</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">Draw 버튼과 More 버튼을 생성하고 통계 창을 띄울 FigureCanvas와 데이터 리스트를 띄울 textEdit을 생성한다. </td>
  </tr>
  <tr>
    <td class="tg-baqh">pushButtonClicked</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">버튼이 눌리면 버튼의 이름에 따라 기능한다. Draw가 입력되면 통게를 그리고, More가 입력되면 가지고 있는 데이터를 모두 띄운다.</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="3">Compare</td>
    <td class="tg-baqh">__init__</td>
    <td class="tg-baqh">self, username, usergender, parent</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">유저의 이름과 성별을 받아와서 FaceRecognition 클래스에 전달한다. 정보를 표시할 레이블과 이미지를 가져오기 위한 QPixmap과 스테이터스 바와 막대그래프 버튼이 선언되어 있다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">buttonClicked</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">막대 그래프 버튼이 눌리면 그래프 창을 띄운다. 그래프 창을 띄울 때 인자로 self.conf_dict를 보내준다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">center</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">버튼의 위치를 가운데로 조정해준다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">Intro</td>
    <td class="tg-baqh">__init__</td>
    <td class="tg-baqh">self, parent</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">사용설명을 위한 텍스트가 저장되어 있고 textEdit이 선언되어 있다.</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="3">Register</td>
    <td class="tg-baqh">__init__</td>
    <td class="tg-baqh">self, parent</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">이미지를 넣기 위한 QPixmap과 정보를 담는 레이블, 성별을 결정하는 QComboBox와 이름을 입력하는 QLineEdit, 그리고 작동 버튼이 선언되어 있다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">buttonClicked</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">버튼이 눌리면 유저의 성별과 이름을 받아와 딕셔너리 형태로 가공해 user_lst에 추가해주고 같은 디렉토리 내에 있는 user_info.txt 파일에 pickle을 이용해 user_lst를 기록한다. user_lst는 클래스 외부에 선언되어 있으며 프로그램이 실행될 때 바로 파일을 읽어와 저장하게 되어있다. 만약 파일이 존재하지 않으면 빈 리스트로 주어진다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">center</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">버튼의 위치를 가운데로 조정해준다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">ComboBox</td>
    <td class="tg-baqh">showPopup</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">updateComb를 이용하기 위해서 사전에 해둬야 하는 설정들이 있다.</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="4">MainWindow</td>
    <td class="tg-baqh">__init__</td>
    <td class="tg-baqh">self, parent</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">배경화면으로 지정할 이미지를 가져오고 버튼, 텍스트 입력창, 항목 선택 바를 생성한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">updateComb</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">ComboBox가 선택이 되면 자동으로 안에 있던 item들을 초기화 하고 새로 user_lst를 스캔하여 item을 등록한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">center</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">버튼의 위치를 가운데로 조정해준다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">buttonClicked</td>
    <td class="tg-baqh">self</td>
    <td class="tg-baqh">None</td>
    <td class="tg-0lax">버튼이 눌리면 버튼의 텍스트에 따라 각각 기능하는데 유저 삭제 기능은 이 함수 안에 구현되어 있다. regist.py에서 가져온 user_lst를 스캔하여 텍스트 입력창에 입력된 유저의 이름과 일치하는 유저를 삭제한다.</td>
  </tr>
</table>

구현 상세 설계
--------------
> ### class FaceRecognition & FaceCapture
<table class="tg">
  <tr>
    <th class="tg-nrix">FaceRecognition</th>
    <th class="tg-nrix">이름</th>
    <th class="tg-nrix">역할, 설명</th>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="10">attribute</td>
    <td class="tg-nrix">self.username</td>
    <td class="tg-cly1">인자로 받아온 유저의 이름을 저장하는 변수이다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">self.usergender</td>
    <td class="tg-cly1">인자로 받아온 유저의 성별을 저장하는 변수이다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">self.face_classifier</td>
    <td class="tg-cly1">xml 파일에 저장되어 있는 데이터를 바탕으로 학습한 얼굴을 찾는 객체를 선언한다. </td>
  </tr>
  <tr>
    <td class="tg-baqh">self.userFolderPath</td>
    <td class="tg-0lax">유저의 사진이 저장되어 있는 디렉토리의 주소를 저장한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">self.userFiles</td>
    <td class="tg-0lax">self.userFolderPath 주소 안에 있는 파일들의 이름을 저장하는 리스트이다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">self.gender_path</td>
    <td class="tg-0lax">유저의 성별을 바탕으로 비교할 사진이 담겨진 디렉토리의 주소를 저장한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">self.otherFiles</td>
    <td class="tg-0lax">self.gender_path 주소 안에 있는 파일들의 이름을 저장하는 리스트이다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">self.Tranning_Data</td>
    <td class="tg-0lax">user 사진의 이미지 데이터를 리스트로 받아와서 리스트를 요소로 갖는 리스트이다. </td>
  </tr>
  <tr>
    <td class="tg-baqh">self.Labels</td>
    <td class="tg-0lax">user 사진에 번호를 매겨 저장하는 리스트이다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">self.model</td>
    <td class="tg-0lax">self.Lables와 self.Tranning_Data를 바탕으로 학습한 모델이다.</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="5">methods</td>
    <td class="tg-baqh">__init__</td>
    <td class="tg-0lax">변수들을 선언하고 저장한다. self.userfiles와 self.userFolderPath를 이용해 유저 사진의 주소를 구하고 데이터를 읽어와 self.Training_Data에 저장한다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">update_data</td>
    <td class="tg-cly1">self.userFolderPath와 self.gender_path를 다시 스캔해서 저장한다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">face_detector</td>
    <td class="tg-cly1">self.face_classifier를 이용해 주어진 img에서 얼굴을 추출해 faces에 저장하고 사이즈를 200 x 200 으로 바꿔 roi에 저장해 원본파일과 함께 출력한다.</td>
  </tr>
  <tr>
    <td class="tg-nrix">compare_face</td>
    <td class="tg-cly1">self.genderPath와 self.otherFiles를 이용해 연예인 사진의 주소를 구하고 이미지를 불러온다. 그리고 face_detector를 이용해 연예인의 얼굴만 추출한 데이터를 self.model를 이용해 유저와의 유사도를 예측한다. 마지막으로 결과값을 연예인의 이름과 짝 지어 딕셔너리 형태로 출력한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">make_file</td>
    <td class="tg-0lax">입력 주소와 출력 주소를 받아 입력 주소에서 얼굴만 찾아서 잘라낸 이미지를 출력주소에 저장한다.</td>
  </tr>
  <tr>
    <th class="tg-baqh">FaceCapture</td>
    <th class="tg-baqh">이름</td>
    <th class="tg-baqh">역할, 설명</td>
  </tr>
  <tr>
    <td class="tg-baqh">attribute</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">-</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="2">methods</td>
    <td class="tg-baqh">face_extractor</td>
    <td class="tg-0lax">이미지를 받아와 흑백으로 전환해 얼굴을 찾고 이미지를 잘라내 출력한다.</td>
  </tr>
  <tr>
    <td class="tg-baqh">capture_face</td>
    <td class="tg-0lax">기본값으로 설정되어 있는 카메라를 통해 이미지를 입력받는다. username을 인자로 받아서 user이름으로 된 디렉토리를 만들고 그 안에 유저의 얼굴만을 잘라낸 사진들을 저장한다.</td>
  </tr>
</table>

> ### class MainWindow

<table class="tg"> <tr> <th class="tg-y0n7">class MainWindow<br></th> <th class="tg-y0n7">이름<br></th> <th class="tg-y0n7">역할, 설명<br></th> </tr> <tr> <td class="tg-nrix" rowspan="14"><br>Attribute<br>(properties)<br></td> <td class="tg-nrix">background<br></td> <td class="tg-cly1">시작 window의 배경화면 이미지를 절대경로를 통해 바인딩한 변수.<br>QSize를 통해 width와 height을 맞춰주었다.</td> </tr> <tr> <td class="tg-nrix">palette<br></td> <td class="tg-cly1">배경화면을 설정해주기 위해 QPalette를 바인딩한 변수. <br>setBrush로 background 이미지를 받음.<br></td> </tr> <tr> <td class="tg-nrix">title <br></td> <td class="tg-cly1">"Face Recognition"이라는 문자열을 갖는 QLabel. <br>setStyleSheet, setFont로 문자열의 색, 글꼴, 글자 사이즈, 볼드체를 설정해주었다.</td> </tr> <tr> <td class="tg-nrix">textinput<br></td> <td class="tg-cly1">QLineEdit을 사용하여 지울 이름을 작성하게 하였다.<br></td> </tr> <tr> <td class="tg-baqh">removebutton<br></td> <td class="tg-0lax">textinput에 적혀져 있는 텍스트에 해당하는 유저를 삭제하는 기능을 하는 버튼이다.<br></td> </tr> <tr> <td class="tg-baqh">enrollmentbutton<br></td> <td class="tg-0lax">Register window를 실행하여 사진을 찍고 유저 등록을 위한 버튼이다.<br></td> </tr> <tr> <td class="tg-baqh">combobox<br></td> <td class="tg-0lax">등록한 유저들을 선택할 수 있는 combobox이다.<br></td> </tr> <tr> <td class="tg-baqh">startbutton<br></td> <td class="tg-0lax">combobox에 선택 된 유저의 결과를 보여주는 버튼이다.<br></td> </tr> <tr> <td class="tg-baqh">introductionbutton<br></td> <td class="tg-0lax">사용설명서의 내용을 담고 있는Intro window를 실행시키기 위한 버튼이다.<br></td> </tr> <tr> <td class="tg-baqh">removelayout<br></td> <td class="tg-0lax">textinput Widget과 removebutton을 추가할 QHBoxLayout이다.<br></td> </tr> <tr> <td class="tg-baqh">resultlayout<br></td> <td class="tg-0lax">combobox Widget과 startbuton을 추가할 QHBoxLayout이다.<br></td> </tr> <tr> <td class="tg-baqh">buttonlayout<br></td> <td class="tg-0lax">removelayout, enrollmentbutton, resultlayout, introductionbutton을 추가할 <br>QVBoxLayout이다.<br></td> </tr> <tr> <td class="tg-baqh">vlayout<br></td> <td class="tg-0lax">title, buttonlayout을 추가할 QVBoxLayout이다.<br></td> </tr> <tr> <td class="tg-baqh">hlayout<br></td> <td class="tg-0lax">addStrech를 통해 vlayout을 한쪽으로 몰아 넣어 줄 QHBoxLayout이다<br></td> </tr> <tr> <td class="tg-baqh" rowspan="4"><br><br><br>methods</td> <td class="tg-baqh">**intit**()</td> <td class="tg-0lax">초기 시작 window를 화면에 띄우는 메소드이다.<br></td> </tr> <tr> <td class="tg-baqh">buttonClicked()</td> <td class="tg-0lax">버튼이 눌리면 버튼의 텍스트에 따라 각각의 기능을 수행하게 만들어 주는 메소드이다.<br></td> </tr> <tr> <td class="tg-baqh">updateCombo<br></td> <td class="tg-0lax">combobox 유저의 이름을 추가하는 메소드이다.<br></td> </tr> <tr> <td class="tg-baqh">center<br></td> <td class="tg-0lax">window를 화면의 중앙에 위치시키는 메소드이다.<br></td> </tr></table>
> ### class Button

<style type="text/css"> .tg {border-collapse:collapse;border-spacing:0;} .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} .tg .tg-cly1{text-align:left;vertical-align:middle} .tg .tg-y0n7{background-color:#efefef;text-align:center;vertical-align:middle} .tg .tg-nrix{text-align:center;vertical-align:middle}</style><table class="tg"> <tr> <th class="tg-y0n7">class Button<br></th> <th class="tg-y0n7">이름<br></th> <th class="tg-y0n7">역할, 설명<br></th> </tr> <tr> <td class="tg-nrix" rowspan="2">methods<br></td> <td class="tg-cly1">**init**()<br></td> <td class="tg-cly1">text와 callback를 인자로 받아 버튼의 텍스트를 text로 하고 <br>callback 해당하는 내용이 버튼이 눌리면 실행되게 한다.</td> </tr> <tr> <td class="tg-nrix">sizeHint</td> <td class="tg-cly1">버튼의 width와 height를 맞춰준다.<br></td> </tr></table>
> ### class ComboBox

<style type="text/css"> .tg {border-collapse:collapse;border-spacing:0;} .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} .tg .tg-lboi{border-color:inherit;text-align:left;vertical-align:middle} .tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle} .tg .tg-fsme{background-color:#efefef;border-color:inherit;text-align:center;vertical-align:middle}</style><table class="tg"> <tr> <th class="tg-fsme">class ComboBox<br></th> <th class="tg-fsme">이름<br></th> <th class="tg-fsme">역할, 설명<br></th> </tr> <tr> <td class="tg-9wq8"><br>Attributes<br>(properties)<br></td> <td class="tg-9wq8">popupAboutToBeShown</td> <td class="tg-lboi">pyatSingal을 바인딩한 변수이다.<br></td> </tr> <tr> <td class="tg-9wq8">methods<br></td> <td class="tg-9wq8">showPopup</td> <td class="tg-lboi">콤보 박스를 클릭할 때마다 자동으로 값을 업데이트 해주는 메소드이다.</td> </tr></table>
> ### class Intro

<table> <tr> <th>class Intro<br></th> <th>이름<br></th> <th>역할, 설명<br></th> </tr> <tr> <td rowspan="3"><br>attribute<br>(properties)<br></td> <td>text<br></td> <td>설명이 포함 되어져 있는 문자열을 바인딩할 변수<br></td> </tr> <tr> <td>introduce<br></td> <td><br>Layout 에 더해줄 Widget이자 text의 내용을 담을 변수.<br>Qt.AlignLeft로 왼쪽 정렬을 해주었다.<br></td> </tr> <tr> <td>mainlayout</td> <td>화면에 표시할 window<br></td> </tr> <tr> <td>methods<br></td> <td>**intit**()<br></td> <td>화면에 사용설명서 창을 띄움<br></td> </tr> </table>
> ### class compare

<style type="text/css"> .tg {border-collapse:collapse;border-spacing:0;} .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} .tg .tg-lboi{border-color:inherit;text-align:left;vertical-align:middle} .tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle} .tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top} .tg .tg-fsme{background-color:#efefef;border-color:inherit;text-align:center;vertical-align:middle} .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}</style><table class="tg"> <tr> <th class="tg-fsme">class Compare<br></th> <th class="tg-fsme">이름<br></th> <th class="tg-fsme">역할, 설명<br></th> </tr> <tr> <td class="tg-9wq8" rowspan="18">Attributes<br>(properties)</td> <td class="tg-9wq8">f<br></td> <td class="tg-lboi">FaceRecognition() 클래스를 바인딩한 변수이다.</td> </tr> <tr> <td class="tg-9wq8">conf_dic<br></td> <td class="tg-lboi">f.compare_face()를 실해하여 userimage와 otherimage를 비교한 결과 값을 <br>딩dictionary 형식으로 return 받은 값을 바인딩한 변수이다.</td> </tr> <tr> <td class="tg-c3ow">conf_rank<br></td> <td class="tg-0pky">conf_dic의 key를 key에 따른 value를 기준으로 정렬시켜 놓은 리스트이다.<br></td> </tr> <tr> <td class="tg-c3ow">userimagebox</td> <td class="tg-0pky"><span style="font-weight:400;font-style:normal">"본인 사진"이라는 문자열을 갖는 QLabel을 바인딩한 변수이다.</span><br><span style="font-weight:400;font-style:normal">setStyleSheet, setFont로 문자열의 색, 글꼴, 글자 사이즈, 볼드체를 설정해주었다</span>.</td> </tr> <tr> <td class="tg-c3ow">resultimagebox<br></td> <td class="tg-0pky"><span style="font-weight:400;font-style:normal">"가장 비슷한 연예인"이라는 문자열을 갖는 QLabel을 바인딩한 변수이다.</span><br><span style="font-weight:400;font-style:normal">setStyleSheet, setFont로 문자열의 색, 글꼴, 글자 사이즈, 볼드체를 설정해주었다</span>.</td> </tr> <tr> <td class="tg-c3ow">userimage</td> <td class="tg-0pky">QPixmap을 활용하여 절대경로를 바탕으로 userimage를 불러왔고<br>scaledToHeight()를 통해 높이 기준으로 이미지를 축소 시켰다.<br></td> </tr> <tr> <td class="tg-c3ow">userimage_label<br></td> <td class="tg-0pky">userimage를 widget으로 변환시켜주기 위해 QLabel을 바인딩 시켜놓음.<br></td> </tr> <tr> <td class="tg-c3ow">vstext<br></td> <td class="tg-0pky"><span style="font-weight:400;font-style:normal">"vs"이라는 문자열을 갖는 QLabel을 바인딩한 변수이다.</span><br><span style="font-weight:400;font-style:normal">setStyleSheet, setFont로 문자열의 색, 글꼴, 글자 사이즈, 볼드체를 설정해주었다.</span></td> </tr> <tr> <td class="tg-c3ow">resultimage<br></td> <td class="tg-0pky"><br>QPixmap을 활용하여 절대경로를 바탕으로, 닮은 비율이 가장 높은 otherimage를<br>불러왔고 scaledToHeight()를 통해 높이 기준으로 이미지를 축소 시켰다.<br></td> </tr> <tr> <td class="tg-c3ow">resultimage_label<br></td> <td class="tg-0pky">resultimage를 widget으로 변환시켜주기 위해 QLabel을 바인딩 시켜놓음.</td> </tr> <tr> <td class="tg-c3ow">resultpercentage<br></td> <td class="tg-0pky">QProgressBar를 활용하여 퍼센테이지를 시각화하였다.<br></td> </tr> <tr> <td class="tg-c3ow">leftbox<br></td> <td class="tg-0pky">userimagebox와 userimage_label을 추가할 QVBoxLayout이다.<br></td> </tr> <tr> <td class="tg-c3ow">midbox<br></td> <td class="tg-0pky">vstext를 추가할 QVBoxLayout이다.</td> </tr> <tr> <td class="tg-c3ow">rightbox<br></td> <td class="tg-0pky">resultimagebox와 resultimage_label을 추가할 QVBoxLayout이다.<br></td> </tr> <tr> <td class="tg-c3ow">staticbutton<br></td> <td class="tg-0pky">버튼이 눌리면 결과값의 통계인 BarGraph window를 표시한다.<br></td> </tr> <tr> <td class="tg-c3ow">optionbox<br></td> <td class="tg-0pky">resultpercentage와 staticbutton을 추가할 QHBoxLayout이다.<br></td> </tr> <tr> <td class="tg-c3ow">mainwindow<br></td> <td class="tg-0pky">leftbox, midbox, rightbox 를 추가할 QHBoxLayout이다.<br></td> </tr> <tr> <td class="tg-c3ow">realmainwindow<br></td> <td class="tg-0pky">mainwindow와 optionbox를 추가할 QVBoxLayout이다.<br></td> </tr> <tr> <td class="tg-c3ow" rowspan="3"><br><br>methods</td> <td class="tg-c3ow">**init**()</td> <td class="tg-0pky">선택된 userimage와 가장 비슷한 otherimgae를 표시해줄 window를 띄우는 메소드이다.<br></td> </tr> <tr> <td class="tg-c3ow">buttonClicked()<br></td> <td class="tg-0pky"><span style="font-weight:400;font-style:normal">버튼이 눌리면 버튼의 텍스트에 따라 각각의 기능을 수행하게 만들어 주는 메소드이다.</span></td> </tr> <tr> <td class="tg-c3ow">center</td> <td class="tg-0pky"><span style="font-weight:400;font-style:normal">window를 화면의 중앙에 위치시키는 메소드이다.</span></td> </tr></table>
> ### class Register

<style type="text/css"> .tg {border-collapse:collapse;border-spacing:0;} .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} .tg .tg-lboi{border-color:inherit;text-align:left;vertical-align:middle} .tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle} .tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top} .tg .tg-fsme{background-color:#efefef;border-color:inherit;text-align:center;vertical-align:middle} .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}</style><table class="tg"> <tr> <th class="tg-fsme">class Register<br></th> <th class="tg-fsme">이름<br></th> <th class="tg-fsme">역할, 설명<br></th> </tr> <tr> <td class="tg-9wq8" rowspan="9"><br>Attributes<br>(properties)<br></td> <td class="tg-9wq8">namelabel<br></td> <td class="tg-lboi"><span style="font-weight:400;font-style:normal">"Name"이라는 문자열을 갖는 QLabel이다.</span><br></td> </tr> <tr> <td class="tg-9wq8">search</td> <td class="tg-lboi">자신의 이름을 쓸 QLineEdit이다.<br></td> </tr> <tr> <td class="tg-9wq8">userimage<br></td> <td class="tg-lboi"><span style="font-weight:400;font-style:normal">QPixmap을 활용하여 절대경로를 바탕으로 userimage를 불러왔고</span><br><span style="font-weight:400;font-style:normal">scaledToHeight()를 통해 높이 기준으로 이미지를 축소 시켰다. </span><br><span style="font-weight:400;font-style:normal">처음에는 회색 빈 화면을 띄우다가 검색 버튼이 눌리고 난 후</span><br><span style="font-weight:400;font-style:normal">userimage로 변경된다.</span><br></td> </tr> <tr> <td class="tg-9wq8">userimage_label</td> <td class="tg-lboi"><span style="font-weight:400;font-style:normal">userimage를 widget으로 변환시켜주기 위해 QLabel을 바인딩 시켜놓음.</span></td> </tr> <tr> <td class="tg-9wq8">progress<br></td> <td class="tg-lboi"><span style="font-weight:400;font-style:normal">QProgressBar를 활용하여 퍼센테이지를 시각화하였다</span></td> </tr> <tr> <td class="tg-9wq8">combo</td> <td class="tg-lboi">"man", "woman" 을 선택할 combobox를 만들었다.</td> </tr> <tr> <td class="tg-9wq8">searchbutton<br></td> <td class="tg-lboi">namelabel, combo 를 바탕으로 buttonClicked()를 실행한다.<br></td> </tr> <tr> <td class="tg-9wq8">rightlayout<br></td> <td class="tg-lboi">namelabel, search, combo, searchbutton, progress를 추가해줄 QVBoxLayout이다.<br></td> </tr> <tr> <td class="tg-9wq8">mainlayout<br></td> <td class="tg-lboi">userimage_label, rightlayout을 추가할 QHBoxLayout이다.<br></td> </tr> <tr> <td class="tg-c3ow" rowspan="3">methods<br></td> <td class="tg-c3ow">**inint**()</td> <td class="tg-0pky">유저를 등록해줄 window를 띄운다.<br></td> </tr> <tr> <td class="tg-c3ow"><br><br>buttonClicked()</td> <td class="tg-0pky">search, combo의 텍스트를 활용하여, 만약 이 값이 존재한다면 덮어씌우고<br>없다면 이를 dictionary로 만들어 user_lst에 append한다. 그 후 이를 "user_info.txt"에 <br> user_lst를 저장하고 사진을 찍는다. 사진을 찍은 후 userimage를 gray에서 <br>본인 이미지로 변환시킨다.<br></td> </tr> <tr> <td class="tg-c3ow">center</td> <td class="tg-0pky"><span style="font-weight:400;font-style:normal">window를 화면의 중앙에 위치시키는 메소드이다.</span></td> </tr></table>
코딩
----------
https://github.com/ehyeok9/Software-Project-II---AD-project

단위 테스트
-----------

시스템 통합
-----------

통합 테스트
-----------
