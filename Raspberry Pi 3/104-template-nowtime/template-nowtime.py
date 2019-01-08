#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO                              #載入PI-IO套件
import subprocess                                    #載入執行外部程式套件
import datetime         #載入時間套件
from flask import Flask, render_template, request
#  載入      網頁製作套件, 網頁指向套件   , POST,GET套件
app = Flask(__name__)


@app.route("/")
def hello():                               #http://192.168.XX.XX/
   now = datetime.datetime.now()    #獲取當前時間並存在變數now
   timeString = now.strftime("%Y-%m-%d %H:%M")     #創時間格式存在timeString
   templateData = {
      'title' : 'HELLO!',                         
      'time': timeString
      }     #創變數templateData字典格式要傳過去前端HTML,'ID':值
   return render_template('main.html', **templateData)   #顯示main.html網頁,放templateData的ID跟值過去
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)