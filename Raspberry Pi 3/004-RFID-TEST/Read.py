#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO			#載入PI-GPIO套件
import SimpleMFRC522			#載入RFID套件

reader = SimpleMFRC522.SimpleMFRC522()	#變數reader = 啟動RFID設置指令

try:
	id, text = reader.read()				#讀取RFID內部資料
	#print(id)								#顯示id內容	
	print(text)								#顯示text內容
finally:									#try:最後要用finally:
	GPIO.cleanup()							#清掉結束GPIO
