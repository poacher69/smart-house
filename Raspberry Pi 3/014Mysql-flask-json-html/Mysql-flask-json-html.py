#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time,datetime                #載入時間套件
from time import strftime           #從time套件載入strftime套件

import RPi.GPIO as GPIO                              #載入PI-IO套件
import subprocess                                    #載入執行外部程式套件
from flask import Flask, render_template, request,redirect, url_for
#  載入      網頁製作套件, 網頁指向套件   , POST,GET套件

from module.database import Database  #從檔案路徑/module/database.py載入class Database:

GPIO.setmode(GPIO.BCM)                    #設定BCM接腳GPIO模式 GPIO2~GPIO26

app = Flask(__name__)


@app.route('/')                    #http://192.168.XX.XX:5000/
def index():                       #首頁function
	print "現在在首頁"			   #PI顯示
	return "Hello world" \
		   "<form method='get' action='/test1'>" \
           "</br>" \
           "<button type='submit'>到溫度頁</button></form>" \
           "<form method='get' action='/led'>" \
           "</br>" \
           "<button type='submit'>到LED頁</button></form>" \
           "<form method='get' action='/rfid'>" \
           "</br>" \
           "<button type='submit'>到RFID頁</button></form>" \
           "<form method='get' action='/mysql'>" \
           "</br>" \
           "<button type='submit'>到Mysql頁</button></form>" \
           "<a href = '/mysql'>用a到MYSQL頁</a>"

@app.route('/mysql')                    #http://192.168.XX.XX:5000/
def mysql():                       #首頁function
 return render_template('mysql_web.html')  #顯示led.html網頁


@app.route('/test')
def result():
   dict = {'phy':'2018/10/14','che':60,'maths':70}
   return render_template('main.html', result = dict)

@app.route('/select_data', methods=['GET','POST'])
def select_data():
  #if request.method == 'GET':
   # user_id = str(request.args.get('id'))
  #else:
   # user_id = str(request.form["id"])

  db = Database()
  #sql_query = "SELECT * FROM inventory WHERE id = %s;" % (user_id)  #打ID只顯示撈回一筆上方if#要拿掉
  sql_query = "SELECT * FROM inventory;"     #撈回inventory全部資料要用,上面if else要#掉
  data_string = db.execute_select(sql_query)
  return render_template('main.html', result = data_string)
  #return data_string + \
  #       "<form method='get' action='/mysql'>" \
  #       "</br>" \
  #       "<button type='submit'>回mysql頁面</button></form>"
  
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)