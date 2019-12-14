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

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#ccc;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#f0f0f0;}
.tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-j844{color:#333333;border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-nrix{text-align:center;vertical-align:middle}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
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





구현 상세 설계
--------------

코딩
----

단위 테스트
-----------

시스템 통합
-----------

통합 테스트
-----------
