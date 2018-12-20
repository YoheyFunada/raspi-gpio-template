#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def main():
  # 使用する出力ピン(GPIO)
  pin_num = 14

  # GPIOピンの定義
  # GPIO番号で指定
  GPIO.setmode(GPIO.BCM)
  # 出力モード
  GPIO.setup(pin_num, GPIO.OUT)

  # 点滅を100回繰り返し
  for i in range(100):
    # 点灯
    GPIO.output(pin_num, GPIO.HIGH)
    print("HIGH")
    # 1秒待機
    time.sleep(1)
    # 消灯
    GPIO.output(pin_num, GPIO.LOW)
    print("LOW")
    # 1秒待機
    time.sleep(1)
    print(i)

  # GPIOピンの設定解除
  GPIO.cleanup()

if __name__ == "__main__":
    main()
