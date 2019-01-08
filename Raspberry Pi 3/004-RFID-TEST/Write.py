#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO			#載入PI-GPIO套件
import SimpleMFRC522			#載入RFID套件

reader = SimpleMFRC522.SimpleMFRC522()	#變數reader = 啟動RFID設置指令

try:
	text = raw_input('New data:')			#變數text=輸入框輸入的值
	print("Now place your tag to write")	#顯示可以放卡片準備寫入	
	reader.write(text)						#RFID寫入指令
	print("Written")						#顯示已成功寫入
finally:									#try:最後要用finally:
	GPIO.cleanup()							#清掉結束GPIO
