#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time					#載入時間套件
import RPi.GPIO as GPIO		#載入PI-GPIO套件

LED_PIN=12					#定義變數LED_PIN=12腳
GPIO.setmode(GPIO.BOARD)	#設定BOARD接腳模式PIN NO.左1,右2到40腳
GPIO.setup(LED_PIN,GPIO.OUT)#設定腳位輸入IN或輸出OUT

try:						#正常程式操作
  while True:
    print "LED is on"		#PI顯示資訊
    GPIO.output(LED_PIN,GPIO.HIGH)	#GPIO HIGH
    time.sleep(1)			#延1秒
    print "LED is off"		#PI顯示資訊
    GPIO.output(LED_PIN,GPIO.LOW)	#GPIO LOW
    time.sleep(1)
except KeyboardInterrupt:	#異常程式跳這段
  GPIO.cleanup()			#GPIO清除