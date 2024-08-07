# IoT-OpenHardware-platform
IoT 오픈하드웨어 플랫폼 활용 리포지토리 ✏️

## 1일차
- 기본적인 이론
    - 옴의 법칙
        - 물체에 흐르는 전류의 세기 (I)는 물체에 걸린 전압(V)에 비례하고, 저항(R)에 반비례한다. => V = IR
        - 전류(I) - 전하의 흐름 (+)->(-) 방향, [A] 단위 
        - 전압(V) - 전기회로에서 전류를 흐르게 하는 능력 [V] 단위 
        - 저항(R) - 전기희 흐름을 방해
    - 키르히호프 법칙
        - 키르히호프 1법칙 : kirchhoff's Current Law(KCL) -전류법칙
            - 회로중의 어떤 분기점에 들어간 전류와 나가는 전류의 합은 같다.
        - 키르히호프 2법칙 : kirchhoff's voltage Law(KVL) - 전압법칙
            - 회로 중의 임의의 폐회로에서 전원전압(기전력)과 부하로 소비되는 전압(전압강하)의 합은 동일해진다.
        
- putty에서 라즈베리파이 PinMap 확인하기
    - putty 창에서 pinout 입력
    - [확인화면]
<figure class="half">  
    <a href="link"><img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi001.png" weight="20"|height="30"></a> 
    <a href="link"><img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi002.png" weight="20"|height="30"></a> 
</figure>

- 실습에 필요한 기본적인 함수
    - GPIO 설정함수
        - GPIO.setmode(GPIO.BOARD) - wPi
        - GPIO.setmode(GPIO.BCM) - BCM
        - GPIO.setup(channel, GPIO.mode)
            - channel: 핀 번호, mode: IN/OUT
        - GPIO.clearup()
    - GPIO 출력함수
        - GPIO.output(channel, state)
            - channel: 핀번호, state: HIGH/LOW or True/False
    - GPIO 입력함수
        - GPIO.input(channel)
            - channel: 핀번호, 반환값: H/L or 1/0 or T/F
    - 시간지연 함수
        - time.sleep(secs)
- led 실습

- 디지털에서 Switch
    - 풀업 저항
        - Vcc에 저항 연결
        - off : input(1), on : input(0)
        - Off 상태일때 A에는 항상 5V의 전압이 걸려 HIGH(1) 값
        - 스위치를 닫아 On 상태가 되면 대부분의 전류는 GND로 흘러 A는 Low(0)값 
    - 풀다운 저항
        - GND에 저항 연결
        - off : input(0), on : input(1)
        - Off 상태일때 A에는 항상 GND와 연결되어 Low값(0) 
        - 스위치를 닫아 on 상태가 되면 전류는 Vcc핀으로 흐르게 되어 A는 High(1)값 
<figure class="half">  
    <p4>[풀업저항]-
        <a href="link"><img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi004.png"></a> 
    </p4>
    <p4>[풀다운저항]-</p4>
        <a href="link"><img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi003.png"></a> 
</figure>

- 실습
    - 스위치 풀다운 
        - 스위치는 서로 마주보고 있는 A와 D가 연결되어 있고 B와 C가 서로 연결
        - A- Vcc 연결, C- GPIO, B- 저항, GND 연결

        ![확인 결과](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi005.png)
    - 스위치 실습
        - 버튼을 누를때마다 led 색이 바뀌는 기능 구현하기

- 부저 실습
    - 음계, 주파수
    - 부저를 이용한 전자 키보드 구현하기
        - 숫자(1~8) 입력시 해당하는 음계 소리 출력
         
## 2일차
- 적외선 감지 센서 실습
    - 동작 인식시 print()함수 이용하여 감지 확인 출력
    - 동작 인식시 led가 켜지는 기능 구현
        - 적외선 감지 센서, led
<figure class="half">  
    <a href="link"><img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi010.png"></a> 
    <a href="link"><img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi009.png"></a> 
</figure>


- 환경설정
    - version 확인
        - python -V
    - 가상환경 생성
        - python -m venv env (생성)
        - source ./env/bin/activate (가상환경으로 들어가기)
        -  deactivate   (빠져나오기)

- 라즈베리파이 GPIO 확인
    - putty 명령창에 sudo git clone https://github.com/WiringPi/WiringPi 입력하여 WiringPi 복사
    - WirionPi 경로로 들어가서 ls입력후 build 확인
    - sudo ./build 입력 후 설치
    - gpio readall 입력으로 확인

    ![확인 결과](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi006.png)

- 초음파 센서 실습
    - print() 함수 이용 거리 출력하기
    - 충돌방지 경고음 구현하기
        - 부저 + 초음파 센서 이용
        - 거리가 5cm 이하일때 경고음 발생
        ```python
        try:
            while True:
                distance = measure()
                if distance <= 5:
                    Buzz.start(50)
                    for i in range(0, len(melody)) :
                        Buzz.ChangeFrequency(melody[i])
                        time.sleep(0.3)
                    Buzz.stop()
                    print("Distance is 5cm under!! : %.2f cm" %distance)
                    time.sleep(1)
                else:
                    print("Distance: %.2f cm" %distance)
        ```
<figure class="half">  
    <a href="link"><img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi008.png"></a> 
    <a href="link"><img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi007.png"></a> 
</figure>

## 3일차
- 릴레이 실습
    - 릴레이 
        - 검출된 정보를 갖고 있는 제어 전류의 유무 또는 방향에 따라 다른 회로를 개폐하는 장치
        - 즉, 입력이 어떤 값에 도달하였을 때 작동하여 다른 회로를 개폐하는 장치로 일종의 자동 스위치
        - 낮은 전압을 이용하여 더 높은 전압을 제어하는데 많이 사용됨
        - 교류, 직류 구분 없이 사용 가능
        - 잡음 발생, 접점 부의가 마모되어 고장 날 수 있음
    - 동작 순서
        - 전원이 공급 -> 코일에 전기가 흘러 자회됨 -> 자화된 전자석에 의해 반대편 스위치 작동 -> 반대편 기기의 전원이 공급

    ![릴레이](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi011.png)
    
    - 실습
        - 릴레이 led 제어하기
            - 릴레이 연결 배선
    
    ![릴레이 연결배선](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi015.png.jpg)

- 모터 + 모터 드라이버 실습
    - 스텝 모터
        - step 상태에서 pulse에 순서를 부여하여 주어진 펄스 수에 비례한 각도만큼 회전하는 모터
        - 한 바퀴의 회전을 많은 수의 스텝으로 나눌 수 있는 직류 전기 모터
        - 입력 신호에 따라 일정 각도를 회전하므로 위치 정보를 반환하지 않고도 현재의 위치 정보를 알 수 있다
    
    ![스텝 모터](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi012.png)
    
    - 실습
        - 기초 실습
        - 기초 실습 for문으로 구현하기
        ```py
        
        step_seq = [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]
        ]

        try:
            while True:
                for seq in step_seq:
                    for pin in range(4):
                        GPIO.output(steps[pin], seq[pin])
                    time.sleep(0.01) 
        ```    

- flask 
    - 파이썬을 통해 웹개발을 할 수 있게 해주는 웹개발 프레임워크
        - 다양한 프레임워크
            - PHP - 라라벨, Node.js - xpress, java - ruby
            - python - flask, django
    - 용량이 작고 사용법이 간단 -> 라즈베리파이에서 쉽게 웹을 통해 gpio 제어 가능
    
    - flask 설치 확인하기 
        - python - from flask import Flask 입력 후 아무 반응 없으면 설치가 되어있는 상태

    - 가상환경 다시 설치 
        -  python -m venv --system-site-packages env
        - 명령어 실행 후 pip list로 확인해보면 라이브러리가 설치된 상태로 가상환경 만들어짐.
    
    -  Flask를 돌리기 위한 파이썬의 기본 폼
        ```py
        from flask import Flask, render_template
        app = Flask(__name__)

        @app.route("/")
        def home():
            return render_template("html파일명.html")

        if __name__=='__main__':
            app.run(host='0.0.0.0')
        ```
    - flask를 돌리기 위한 규칙
        - Flask를 돌리는 코드 파일명(위에 적혀있는 코드가 속해져있는 파일)은 'app.py'여야 한다.
        - html는- 'template' 디렉토리 하위에 속해져있었야한다
        - 이미지 파일 등을 넣어야하는 경우 파일들은 'static' 디렉토리 하위에 속해져있어야한다.

- Flask 실습 
    - 웹페이지 구현하기
        - flask로 문자 출력

            ![웹페이지 화면](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi013.png)

        - led 제어 페이지 구현하기
            - url 접속을 /led/on, /led/off로 접속하면 led를 on, off하는 웹페이지
        
        - <state> 사용하여 led 제어 페이지 구현하기
            ```py
            @app.route("/led/<state>")
            def control_led(state):
                if state == "on":
                    GPIO.output(led, True)
                    return "LED ON"
                elif state == "off":
                    GPIO.output(led, False)
                    return "LED OFF"
                elif state == "clear":
                    GPIO.cleanup()
                    return "GPIO Cleanup()"
            ```    
            - 192.168.5.3:10011/led/~~ 로 접속하면 led를 제어할 수 있음

        - GET(방식)
            - 웹 서비스 개발에 사용하는 메서드, 서버에 요청하는 메서드
            - URL 뒤의 파라미터를 추가하여 데이터를 전달
            - 간단하고 직관적이지만 URL에 데이터가 노출되어 보안성이 낮음
            - 예시 - www.example.com?id=mommoo&pass=1234


        ![GET방식](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi014.png)

## 4일차
- flask 실습 계속
    - flask, html 연동하여 post 방식으로 웹 구현하기
        ```py
        from flask import Flask, request, render_template #추가하기
        @app.route('/')
        def home () :
            return render_template("index.html")
        ```
        - remder_template() : html파일을 text 형태로 반환해주는 함수
        - index.html 파일 위치 - 코드파일이 있는 폴더에 template 폴더 생성 후 폴더 안에 위치 
        - led 제어화면 구현 
            
            <img src="https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi001.gif">

- Picamera2 실습
    - 설치 확인
        - pip list 명령창에 입력 후 확인
    - 실습
        - 실행시 사진 촬영, test.jpg 생성
        
        ![실행화면]

        - 버튼 클릭 시 촬영되고 현재 시간이 파일명인 .jpg 이미지 파일 저장

        ![실행화면](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi015.png)

        ![실행화면](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi016.png)


- 4-digit, 7-segement display, FND
    - 공통 단자를 COMn으로 표기, COM1~ COM4까지 사용
    - a ~ g, dp등 총 8개의 세그먼트 핀이 존재
    - 총 12핀으로 구성

        ![7-seg 핀 구성](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi017.png)
    
    - 방식
        - 공통 음극(Common Cathod)방식
            - COM1 ~ COM4를 모두 (-) 신호, 데이터 신호는 (+) 신호
        
        ![Common Cathod 회로구성](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi018.png)
        
        - 공통 양극(Common Anode) 방식
            - COM1 ~ COM4를 모두 (+) 신호, 데이터 신호는 (-) 신호
    
    - Common Cathod방식 실습
        - 하나의 com만 연결하여 실습 진행, 실습 진행 전 음극인지 양극인지 확인하기 
            - COM1에 GND, 데이터 신호 핀 아무곳에 Vcc 연결 했을때 led 불이 켜지면 음극 방식

        - 1을 5초동안 출력하는 display 구현하기
        
        - 0 ~ 9 까지 1초마다 숫자가 바뀌는 display 구현하기
            ```py
            def display_digit(number):
             if number in digits:
                for segment in segments.values():  # 숫자를 표시하기 전에 모든 led off 시키기
                     GPIO.output(segment, False)

                 for segment in digits[number]:
                    GPIO.output(segments[segment], True)
            ```
            - 메인 실행문은 반복문으로 구현


https://github.com/Juhyi/IoT-OpenHardware-platform/assets/158007405/1cfc31ad-518d-4a7f-8bda-8221f2398004


## 5일차
- 4-digit 7-segment 실습 계속
    - 버튼을 누를때마다 카운트되는 기능 구현하기
        - 스위치는 풀 다운으로 연결, 7-seg 로 번호 표현은 dictionary 구현
        - 스위치가 false가 되면 count를 1 증가시키고 (0~9) 10으로 나눈값을 count에 대입하여 count의 수를 display
    ![실행결과](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi019.png)

    - 4-digit 모두 이용하여 1~9999 버튼을 누르면 1씩 증가하는 기능 구현
        - 각각의 digit을 제어하기 위해서 comN에 GPIO 연결
        - COM 핀으로 FND를 선택하고 8개의 segment 신호를 받아서 숫자 표기
        - 빠른 속도로 신호를 전달하여 4개의 FND에 신호가 다 들어오는 것처럼 보임
        ```py
         for _ in range(100):  # 100번 반복으로 디스플레이 깜빡임현상 줄여줌
            display_digit(thousands, 0)
            display_digit(hundreds, 1)
            display_digit(tens, 2)
            display_digit(ones, 3)
        ```
        - 구현 방법 
            - 1. count 숫자값을 단위로 나눠 몫을 각 seg에 전달하여 출력
            - 2. 각자리를 index로 보고 자릿수가 넘어가면 index값을 증가시켜서 다음 seg에 표현

        - 버튼을 누르고 있지 않아도 display에 숫자를 계속 나타내기 
            - GPIO.input(swtich) == False를 사용하지 않고
            - newSw, oldSw를 사용하여 구현하면 된다.
        
        

https://github.com/Juhyi/IoT-OpenHardware-platform/assets/158007405/3376ed55-b6f5-41ca-848b-0ce34c93d443


## 6일차
- FND 실습 계속
    - 방법 3. 
        - 디스플레에 표시할 숫자의 세그먼트 데이터
            - 각 수자를 표시하기 위한 이진 데이터 값 리스트로 선언
        - 7-seg 디스플레이에 숫자 출력 함수
            ```py
            def fndOut(data, sel):
            for i in range(0, 7):
                GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
            for j in range(0, 4):
                    if j == sel:
                        GPIO.output(fndSels[j], 0)
                    else:
                        GPIO.output(fndSels[j], 1)
            ```
            - 인자로 받은 data값의 숫자 표시 & 인지로 받은 sel (comN의 핀)을 on 나머지는 off -> 
        - 메인 루프
            - count 수를 자리수의 수를 d1, d10, d100, d1000으로 전달해줌    
            - fndOut()의 매개변수로 수와 자릿수를 넘겨줌
            - for _ in range(50) 을 사용하여 display에 표시되는 속도 조절

- PyQt
    - C++로 작성된 Qt 프레임워크의 파이썬 바인딩. (바인딩 - 어떤 프로그래밍 언어에서도 사용할 수 있게 만드는 것을 의미)
    - 장점
        - 시각적으로 괜찮은 디자인, 직관적인 GUI 제공
        - 실행 파일 형식으로 소프트웨어를 배포하는 것이 가능, 통합배포
        - 크로스 플랫폼
        - 라이브러리 충돌이슈 최소화
    
    - 설치
        - pip 명령어로 설치 가능 
        ```
        pip install pyqt6
        ```
        - Python v3.6.1 이하인 경우에는 pyqt6 설치 불가능
            - 방안
                1. python 버전 업데이트
                2. pyqt5 설치 (나는 pyqt5로 실습할거임)

    - 모듈  
        - 주요 모듈
            - QtCore: 비 GUI 기능(타이머, 파일 I/O, 스레드)에 필요한 클래스들을 포함
            - QtGui: 기본적인 GUI 기능을 제공하는 클래스들이 포함
            - QtWidgets: 사용자 인터페이스 위젯이 포함된 모듈
            - QtNetwork: 네트워크 프로그래밍과 관련된 클래스들이 포함
        - 개발 도구
            - PyQt Designer: GUI 디자인을 위한 드래그 앤 드롭 인터페이스 도구
            - PyQt Linguist: 애플리케이션의 다국어 지원을 위한 도구

- PyQt 기본 코드
    - 관련 패키지 import
        ```py
        import sys
        from PyQt5.QtWigets import*
        ```
        - 파이썬 내장 라이브러리에 존재하는 sys모듈 import
            - 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
        - PyQt5패키지의 QtWigets 모듈에서 전체를 가져오는 코드 import*
    - PyQt 필수 객체 생성 - QApplication(sys.argv)
        ```py 
        app = QApplication(sys.argv)
        ```
        - app이란 이름의 객체 생성
        - 무조건 써야하는 클래스. 현재 소스코드 파일에 대한 경로를 담고 있는 리스트(sys.argv)를 클래스의 생성자(초기화 메서드, __init__)로 전달해주어야 함.
        - argv : 가변적인 개수의 문자열을 의미
    - 기능 없는 window(창) 구현
        ```py
        window = Qwindget()  # 창의 껍데기 생성
        window.show()   # 창 띄우기
        ```
    - 닫기 버튼을 누를때까지 계속 실행
        ```py
        app.exec_()
        ```

- PyQt 실습
    - pip list 명령어로 설치 확인하기 
    - vncserver-virtural vnc 열기
    - sudo apt install qttools5-dev-tools 로 도구 설치
    - vnc에서 Qt-Designer에서 작업 시작

## 7일차
- 개인 평가 진행
    - pyqt5을 이용하여 지금까지 실습한 센서 rasPi에서 진행
    
