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
- 
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


- 스위치 풀다운 실습
    - 스위치는 서로 마주보고 있는 A와 D가 연결되어 있고 B와 C가 서로 연결
    - A- Vcc 연결, C- GPIO, B- 저항, GND 연결

    ![확인 결과](https://github.com/Juhyi/IoT-OpenHardware-platform/blob/main/imges/raspi005.png)


- 인터럽트(interrupt)
    - 우선순위

- 부저 실습
    - 음계, 주파수
    - 부저를 이용한 전자 키보드 구현하기
        - 숫자(1~8) 입력시 해당하는 음계 
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
