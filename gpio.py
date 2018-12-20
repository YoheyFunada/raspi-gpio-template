# coding: UTF-8
import RPi.GPIO as GPIO  #GPIOにアクセスするライブラリをimportします。
import time


GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。
GPIO.setup(15,GPIO.OUT) #BCMの15番ピン、物理的には10番ピンを出力に設定します。
GPIO.setup(2,GPIO.IN)   #BCM 2番ピンを入力に設定します。

try:
        while True:
                if GPIO.input(2) == GPIO.LOW:
                        GPIO.output(15,GPIO.HIGH)
                else:
                        GPIO.output(15,GPIO.LOW)
                time.sleep(0.1)
except KeyboardInterrupt:
        GPIO.cleanup()