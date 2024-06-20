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
- 스위치
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
- 스위치 풀다운 실습
    - 스위치는 서로 마주보고 있는 A와 D가 연결되어 있고 B와 C가 서로 연결
    - A- Vcc 연결, C- GPIO, B- 저항, GND 연결

- 인터럽트(interrupt)
    - 우선순위
