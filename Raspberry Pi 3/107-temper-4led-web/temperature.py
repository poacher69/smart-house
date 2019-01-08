#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time,datetime                #載入時間套件
from time import strftime           #從time套件載入strftime套件

import RPi.GPIO as GPIO                              #載入PI-IO套件
import subprocess                                    #載入執行外部程式套件
from flask import Flask, render_template, request,redirect, url_for
#  載入      網頁製作套件, 網頁指向套件   , POST,GET套件

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)                    #設定BCM接腳GPIO模式 GPIO2~GPIO26

#創一個pins字典名,PI腳號:名稱和接腳狀態
pins = {
   27 : {'name' : 'led1', 'state' : GPIO.LOW},
   22 : {'name' : 'led2', 'state' : GPIO.LOW},
   23 : {'name' : 'led3', 'state' : GPIO.LOW},
   24 : {'name' : 'led4', 'state' : GPIO.LOW}
   }

#定義腳位OUTPUT,初始為LOW
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)




@app.route('/')                    #http://192.168.XX.XX:5000/
def index():                       #首頁function
	print "現在在首頁"			   #PI顯示
	return "Hello world" \
		   "<form method='get' action='/test1'>" \
           "</br>" \
           "<button type='submit'>到溫度頁</button></form>" \
           "<form method='get' action='/led'>" \
           "</br>" \
           "<button type='submit'>到LED頁</button></form>"

            #顯示Hello,按鍵到/test1


@app.route('/test1')                    #http://192.168.XX.XX:5000/
def test1():                       #首頁function
	
#for num in range(5):
	#while  True:
		now=strftime("%H:%M:%S")          #定義now=現在時間指令
		#print now

		file=open("/sys/bus/w1/devices/28-031721667fff/w1_slave")#定義file=開溫度的檔案路徑
		text=file.read()    #定義text=讀檔案內的資料存在text
		file.close          #檔案關閉
		#print text

		secondline=text.split("\n")[1]  #用("\n")換行篩選第[0]第1行[1]第2行
		#print secondline               #PI顯示測試看有沒抓對行

		tempdata=secondline.split(" ")[9] #用(" ")空格篩選第[0]第1個[1]第2個~[9]第10個
		#print tempdata                   #PI顯示測試看有沒抓對資料t=27500
		temp=float(tempdata[2:])          #轉成浮點抓第3碼開始的數字
		#print temp                       #PI顯示測試抓對資料嗎27500
		temp=temp/1000                    #27500/1000=27.5
		#print temp                       #PI顯示測試抓對資料嗎27.5

		print "現在時間是:" + now + "　溫度=" + str(temp)   #PI顯示現在時間跟溫度
		#time.sleep(1)

		return "現在時間是:" + now + "　溫度=" + str(temp) + \
			   "<form method='get' action='/'>" \
               "</br>" \
               "<button type='submit'>回首頁</button></form>"#PI顯示現在時間跟溫度

@app.route('/led')                    #http://192.168.XX.XX:5000/
def led():                       #首頁function
	#首頁先對每個接腳讀取載入狀態:
      for pin in pins:
            pins[pin]['state'] = GPIO.input(pin)

      #定義templateData變數為pin字典的內容

      templateData = {
      'pins' : pins
      }
      #templateData是從HTML回傳過來的值
      return render_template('led.html', **templateData)    #回傳回首頁網頁

@app.route("/<changePin>/<action>")
def action(changePin, action):
   changePin = int(changePin)                #int定義
   deviceName = pins[changePin]['name']
   if action == "on":
      GPIO.output(changePin, GPIO.HIGH)      # Set the pin high:
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."
   if action == "toggle":
      # Read the pin and set it to whatever it isn't (that is, toggle it):
      GPIO.output(changePin, not GPIO.input(changePin))
      message = "Toggled " + deviceName + "."

   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   templateData = {
      'message' : message,
      'pins' : pins
   }

   return render_template('led.html', **templateData)


#@app.route('/led')                    #http://192.168.XX.XX:5000/
#def led():                       #首頁function
#	return render_template('led.html')   #顯示led.html網頁

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0') 