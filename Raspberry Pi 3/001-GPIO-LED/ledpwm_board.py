#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time                   #載入時間套件
import RPi.GPIO as GPIO       #載入PI-GPIO套件

LED_PIN=12                    #定義變數LED_PIN=12腳
GPIO.setmode(GPIO.BOARD)      #設定BOARD接腳模式PIN NO.左1,右2到40腳
GPIO.setup(LED_PIN,GPIO.OUT)  #設定腳位輸入IN或輸出OUT
pwm=GPIO.PWM(LED_PIN,50)
#50=>1/50=0.02
#0.5=>1/0.5=2
pwm.start(0)#1~100

try:                          #正常程式操作
  while True:
    for dc in range(0,101,5):
      print dc
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.1)
    for dc in range(100,-1,-5):
      print dc
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.1)
except KeyboardInterrupt:     #異常程式跳這段
  pwm.stop()                  #GPIO清除pwm停止
  GPIO.cleanup()              #GPIO清除