#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO                              #載入PI-IO套件
import subprocess                                    #載入執行外部程式套件
from flask import Flask, render_template, request
#  載入      網頁製作套件, 網頁指向套件   , POST,GET套件
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)                    #設定BCM接腳GPIO模式 GPIO2~GPIO26
GPIO.setup(18, GPIO.OUT)                  #設定腳位輸入或輸出
GPIO.output(18, GPIO.LOW)                 #初始腳位為LOW電位

#創一個pins字典名,PI腳號:名稱和接腳狀態
pins = {
   27 : {'name' : 'led1', 'state' : GPIO.LOW},
   22 : {'name' : 'led2', 'state' : GPIO.LOW},
   23 : {'name' : 'led3', 'state' : GPIO.LOW}
   }
 
#定義腳位OUTPUT,初始為LOW
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)



@app.route("/")
def main():                               #http://192.168.XX.XX/
      #首頁先對每個接腳讀取載入狀態:
      for pin in pins:
            pins[pin]['state'] = GPIO.input(pin)

      #定義templateData變數為pin字典的內容

      templateData = {
      'pins' : pins
      }
      #templateData是從HTML回傳過來的值
      return render_template('main.html', **templateData)    #回傳回首頁網頁


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

   return render_template('main.html', **templateData)
  
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)