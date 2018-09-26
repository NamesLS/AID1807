# alarm.py
import time
import signal

signal.alarm(3)
time.sleep(2)
signal.alarm(5)

signal.pause()

while True:
    time.sleep(1)
    print("等待时钟信号...")