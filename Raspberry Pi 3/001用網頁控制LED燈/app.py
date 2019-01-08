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

@app.route("/")
def main():                               #http://192.168.XX.XX/
   return render_template('main.html')    #回傳回首頁網頁

@app.route("/led/on")
def led_on():                             #http://192.168.XX.XX/led/on
   GPIO.output(18, GPIO.HIGH)             #燈ON
   return render_template('main.html')    #回傳回首頁網頁

@app.route("/led/off")
def led_off():                            #http://192.168.XX.XX/led/off
   GPIO.output(18, GPIO.LOW)              #燈OFF
   return render_template('main.html')    #回傳回首頁網頁

@app.route("/lcd")
def lcd():                                #http://192.168.XX.XX/led/lcd
   line1 = request.args.get('line1')      #HTML傳過來的值'line1'
   line2 = request.args.get('line2')      #HTML傳過來的值'line2'
   subprocess.call(["python", "lcd1602.py", line1, line2])
   return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)