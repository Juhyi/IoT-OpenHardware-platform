# IoT-OpenHardware-platform
IoT 오픈하드웨어 플랫폼 활용 레포지토리

## 1일차
- 기본적인 이론
    - 옴의 법칙
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