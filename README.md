# IoT-OpenHardware-platform
IoT 오픈하드웨어 플랫폼 활용 레포지토리

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

        ![실행화면](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi016.png)
    
    - 방식
        - 공통 음극(Common Cathod)방식
            - COM1 ~ COM4를 모두 (-) 신호, 데이터 신호는 (+) 신호
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

            
