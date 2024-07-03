import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
steps = [16, 12, 25, 22]
steps_per_revolution = 2048  # 한 바퀴 회전에 필요한 스텝 수 (28BYJ-48 스텝 모터 기준)

# 스텝 순서 (반시계 방향)
step_seq = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]

# 초기화 변수
current_angle = 0.0
step_angle = 5.625 / 64 

def start_motor(self):
    self.timer.start(100)

def update_motor(self):
    global current_angle

    for seq in step_seq:
        for pin in range(4):
            GPIO.output(steps[pin], seq[pin])
        time.sleep(0.01)

        current_angle += step_angle
        self.angle_label.setText(f"Curent Angle: {current_angle:.2f}")

def closeEvent(self, event):
    self.timer.stop()
    GPIO.cleanup()
    event.accept()