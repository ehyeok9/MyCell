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
--------------------------------

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

코딩
----------

https://github.com/ehyeok9/Software-Project-II---AD-project

단위 테스트
-----------

시스템 통합
-----------

통합 테스트
-----------
