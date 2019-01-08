#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time,datetime                #載入時間套件
from time import strftime           #從time套件載入strftime套件

import RPi.GPIO as GPIO                              #載入PI-IO套件
import subprocess                                    #載入執行外部程式套件
from flask import Flask, render_template, request,redirect, url_for
#  載入      網頁製作套件, 網頁指向套件   , POST,GET套件

import SimpleMFRC522      #載入RFID套件

from module.database import Database  #從檔案路徑/module/database.py載入class Database:

reader = SimpleMFRC522.SimpleMFRC522()  #變數reader = 啟動RFID設置指令
GPIO.setmode(GPIO.BCM)                    #設定BCM接腳GPIO模式 GPIO2~GPIO26

app = Flask(__name__)


#LED設定接腳定義-start
#創一個pins字典名,PI腳號:名稱和接腳狀態LED控制設定-start
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
#LED設定接腳定義-end



@app.route('/')                    #http://192.168.XX.XX:5000/
def index():                       #首頁function
	print "現在在首頁"			   #PI顯示
	return " Smart Home</br> Iot Of Things" \
		   "<form method='get' action='/test1'>" \
           "</br>" \
           "<button type='submit'>溫度頁面</button></form>" \
           "<form method='get' action='/led'>" \
           "</br>" \
           "<button type='submit'>LED頁面</button></form>" \
           "<form method='get' action='/rfid'>" \
           "</br>" \
           "<button type='submit'>RFID頁面</button></form>" \
           "<form method='get' action='/mysql'>" \
           "</br>" \
           "<button type='submit'>Mysql頁面</button></form>" \
           "<form method='get' action='/webcam'>" \
           "</br>" \
           "<button type='submit'>Webcam頁面</button></form>" \
           "</br>" \
           "&emsp;&nbsp;&nbsp;APP Inventor Database \
           &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;APP Inventor Led Control" \
           "</br>" \
           "<img src='https://i.imgur.com/bMSnqSV.jpg'width='200' height='200'/></img>" \
           "&emsp;&emsp;&emsp;&emsp;" \
           "<img src='https://i.imgur.com/bMSnqSV.jpg'width='200' height='200'/></img>" \
           "</br></br></br></br></br>" \
           "&emsp;&nbsp;&emsp;&nbsp;Android Studio APP" \
           "</br>" \
           "<img src='https://i.imgur.com/bMSnqSV.jpg'width='200' height='200'/></img>" 
           

           #"<a href='http://192.168.63.10:8081/'>連到pcnet logo</a>"

            #顯示Hello,按鍵到/test1

########################溫度顯示頁-start
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
               "<img src='https://i.imgur.com/fYz1bxg.jpg'width='200' height='200'/></img>" \
               "<p>" \
               "<button type='submit'>回首頁</button></form>"#PI顯示現在時間跟溫度

########################溫度顯示頁-end

###################################################################

########################LED控制頁-start
@app.route('/led')                    #http://192.168.XX.XX:5000/
def led():                       #首頁function
	#首頁先對每個接腳讀取載入狀態:
      #GPIO.setmode(GPIO.BCM)                    #設定BCM接腳GPIO模式 GPIO2~GPIO26
      for pin in pins:
            pins[pin]['state'] = GPIO.input(pin)

      #定義templateData變數為pin字典的內容

      templateData = {
      'pins' : pins
      }
      #templateData是從HTML回傳過來的值
      return render_template('led.html', **templateData)    #回傳LED網頁,並傳'pins'值過去

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

########################LED控制頁-end

##################################################################

########################RFID頁面-start
@app.route('/rfid')               #http://192.168.XX.XX:5000/rfid
def rfid():                       #function
	return "RFID Page" \
       "<form method='get' action='/rfid/write'>" \
           "</br>" \
           "<button type='submit'>RFID寫入</button></form>" \
           "<form method='get' action='/rfid/read'>" \
           "</br>" \
           "<button type='submit'>RFID讀取</button></form>" \
           "<form method='get' action='/rfid/data'>" \
           "</br>" \
           "<button type='submit'>資料庫讀取RFID刷卡資料</button></form>" \
           "<form method='get' action='/'>" \
           "</br>" \
           "<img src='https://i.imgur.com/2H1gpZ6.jpg'width='200' height='200'/></img>" \
           "</br>" \
           "<button type='submit'>回首頁</button></form>"

@app.route('/rfid/data', methods=['GET','POST'])
def rfid_data():
  #if request.method == 'GET':
   # user_id = str(request.args.get('id'))
  #else:
   # user_id = str(request.form["id"])

  db = Database()
  #sql_query = "SELECT * FROM inventory WHERE id = %s;" % (user_id)  #打ID只顯示撈回一筆上方if#要拿掉
  sql_query = "SELECT * FROM rfid;"     #撈回inventory全部資料要用,上面if else要#掉
  data_string = db.execute_select(sql_query)
  return render_template('rfid_mysql_data.html', result = data_string)



#########RFID-write-start
@app.route('/rfid/write', methods=['GET', 'POST'])  #http://192.168.XX.XX:5000/rfid/write
def rfid_write():                       #首頁function
  if request.method == 'POST':
    text =request.form.get('username1')     #變數text=輸入框輸入的值
    print("Now place your tag to write")  #PI顯示可以放卡片準備寫入  
    reader.write(text)            #RFID寫入指令
    print("Written")            #PI顯示已成功寫入
    #GPIO.cleanup()              #清掉結束GPIO
    return redirect(url_for('rfid_write_hello', username2=request.form.get('username1')))
    #如果收到rfid_write.html傳來的POST,導向到def rfid_write_hello頁面 ,username1是HTML傳過來的資料

  return render_template('rfid_write.html')  #http://192.168.XX.XX:5000/rfid/write顯示rfid_write.html網頁

@app.route('/hello/<username2>')
def rfid_write_hello(username2):
  return render_template('hello.html', username5=username2)  #顯示hello.html網頁,放username5的值過去

#########RFID-write-end

#########RFID-read-start

@app.route('/rfid/read')                    #http://192.168.XX.XX:5000/
def rfid_read():                       #首頁function
      return "請將卡片放置到RFID讀寫器上" \
             "<form method='get' action='/rfid/read_data'>" \
             "</br>" \
             "<button type='submit'>送出</button></form>" \
             "<form method='get' action='/rfid'>" \
             "<button type='submit'>回RFID頁</button></form>"

@app.route('/rfid/read_data')                    #http://192.168.XX.XX:5000/
def rfid_read_data():                       #首頁function
  #try:
  #if request.method == 'POST':
    i = datetime.datetime.now()                         #定義i=時間套件
    nowdate = ("%s/%s/%s" % (i.year, i.month, i.day))   #日期
    nowtime = ("%s:%s:%s" % (i.hour,i.minute,i.second)) #時間
    id, text = reader.read()        #讀取RFID內部資料
    #print(id)                #PI顯示id內容 
    print(text)               #PI顯示text內容
    db = Database()           #定義db=檔案Database()
    sql_query = ("INSERT INTO rfid (name,date,time) VALUES (%s, %s, %s)") #SQL語法上傳資料到rfid資料表
    db.execute(sql_query, (text,nowdate,nowtime)) #上傳到DB的值

  #finally:                  #try:最後要用finally:
      #GPIO.cleanup()              #清掉結束GPIO
    return "RFID Read OK!!</br>" \
           " Hello!! " + text + "</br>" \
           "刷卡資料已上傳到Mysql" \
           "<form method='get' action='/rfid'>" \
           "</br>" \
           "<button type='submit'>回RFID頁</button></form>"

#########RFID-read-end

#########RFID頁面-end

####################################################

#########Mysql頁面-start

@app.route('/mysql')                    #http://192.168.XX.XX:5000/
def mysql():                       #首頁function
 return render_template('mysql_web.html')   #顯示led.html網頁

@app.route('/add_data', methods=['GET','POST'])
def add_data():
  if request.method == 'GET':
    name = str(request.args.get('name'))
    quantity = str(request.args.get('quantity'))
  else:
    name = str(request.form["name"])
    quantity = str(request.form["quantity"])

  db = Database()
  sql_query = ("INSERT INTO inventory (name, quantity) VALUES (%s, %s)")
  db.execute(sql_query, (name, quantity))
  return "name: " + name + '</br>' + "quantity: " + quantity + '</br>' + "add OK" + \
         "<form method='get' action='/mysql'>" \
         "</br>" \
         "<button type='submit'>回mysql頁面</button></form>"


@app.route('/update_data', methods=['GET','POST'])
def update_data():
  if request.method == 'GET':
    user_id = str(request.args.get('id'))
    name = str(request.args.get('name'))
    quantity = str(request.args.get('quantity'))
  else:
    user_id = str(request.form["id"])
    name = str(request.form["name"])
    quantity = str(request.form["quantity"])

  db = Database()
  sql_query = "UPDATE inventory SET quantity = %s, name = %s WHERE id = %s;"
  db.execute(sql_query, (quantity,name,user_id))
  return "id: " + user_id +'</br>' +"name: " + name + '</br>' + "quantity: " + quantity + '</br>' + \
         "update_data OK" + \
         "<form method='get' action='/mysql'>" \
         "</br>" \
         "<button type='submit'>回mysql頁面</button></form>"

@app.route('/delete_data', methods=['GET','POST'])
def delete_data():
  if request.method == 'GET':
    user_id = str(request.args.get('id'))
  else:
    user_id = str(request.form["id"])

  db = Database()
  sql_query = "DELETE FROM inventory WHERE id = %s;"
  db.execute(sql_query,(user_id,))
  print("ID:%s delete ok" % user_id)      #PI顯示
  return "id: " + user_id +'</br>' + "delete_data OK" + \
         "<form method='get' action='/mysql'>" \
         "</br>" \
         "<button type='submit'>回mysql頁面</button></form>"

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
  return render_template('inventory_mysql_data.html', result = data_string)

#########Mysql頁面-end



@app.route('/webcam')                    #http://192.168.XX.XX:5000/
def webcam():                       #首頁function
 return render_template('webcam.html')   #顯示led.html網頁


#########Mysql頁面-end

#@app.route('/led')                    #http://192.168.XX.XX:5000/
#def led():                       #首頁function
# return render_template('led.html')   #顯示led.html網頁

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0') 