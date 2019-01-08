#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask, render_template	#載入網頁製作套件, 網頁指向套件
from flask import request, url_for			#載入POST,GET套件

import mysql.connector
from mysql.connector import errorcode
import json									#載入json套件
import time					#載入時間套件

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('api_web.html')

@app.route('/add_data', methods=['GET','POST'])			#網頁使用GET,POST方法
def add_data():
	if request.method == 'GET':
		name = str(request.args.get('name'))			#GET模式傳資料指令
		quantity = str(request.args.get('quantity'))	#GET模式傳資料指令
	else:
		name = str(request.form["name"])				#POST模式傳資料指令
		quantity = str(request.form["quantity"])		#POST模式傳資料指令

	#print name					#測試有沒傳到PI
	#print quantity 			#測試有沒傳到PI
	#return "ok"


	config = {
			'host':'localhost',
			'user':'root',
			'password':'1234',
			'database':'mydatabase'
		}

	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with the user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cursor = conn.cursor()
		sql_query = ("INSERT INTO inventory (name, quantity) VALUES (%s, %s)")
		cursor.execute(sql_query, (name, quantity))
		conn.commit()
		print("Inserted",cursor.rowcount,"row(s) of data.")
		#Cleanup
		cursor.close()
		conn.close()
		print("insert data")
		return render_template('api_web.html')

##################################################################################

@app.route('/update_data', methods=['GET','POST'])
def update_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))			#GET模式傳資料指令
		name = str(request.args.get('name'))			#GET模式傳資料指令
		quantity = str(request.args.get('quantity'))	#GET模式傳資料指令
	else:
		user_id = str(request.form["id"])				#POST模式傳資料指令
		name = str(request.form["name"])				#POST模式傳資料指令
		quantity = str(request.form["quantity"])		#POST模式傳資料指令

	# print user_id
	# print name				#測試有沒傳到PI
	# print quantity 			#測試有沒傳到PI
	# return "ok"


	config = {
			'host':'localhost',
			'user':'root',
			'password':'1234',
			'database':'mydatabase'
		}

	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with the user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cursor = conn.cursor()
		#cursor.execute("UPDATE inventory SET quantity = %s, name = %s WHERE id = %s;",(quantity,name,user_id))	#第1種寫法
		sql_query = "UPDATE inventory SET quantity = %s, name = %s WHERE id = %s;"
		cursor.execute(sql_query, (quantity,name,user_id))
		conn.commit()
		#Cleanup
		cursor.close()
		conn.close()
		print("Done.update ok")
	return render_template('api_web.html')
##########################################################################################


@app.route('/delete_data', methods=['GET','POST'])
def delete_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))			#GET模式傳資料指令
	else:
		user_id = str(request.form["id"])				#POST模式傳資料指令

	# print user_id
	# print name					#測試有沒傳到PI
	# print quantity 			#測試有沒傳到PI
	# return "ok"


	config = {
			'host':'localhost',
			'user':'root',
			'password':'1234',
			'database':'mydatabase'
		}

	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with the user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cursor = conn.cursor()
		#cursor.execute("UPDATE inventory SET quantity = %s, name = %s WHERE id = %s;",(quantity,name,user_id))	#第1種寫法
		sql_query = ("DELETE FROM inventory WHERE id = %s;")
		cursor.execute(sql_query, (user_id,))
		conn.commit()
		#Cleanup
		cursor.close()
		conn.close()
		print("Done.")
	return render_template('api_web.html')
###################################################################

@app.route('/select_data', methods=['GET','POST'])
def select_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))			#GET模式傳資料指令
	else:
		user_id = str(request.form["id"])				#POST模式傳資料指令

	# print user_id
	# print name					#測試有沒傳到PI
	# print quantity 			#測試有沒傳到PI
	# return "ok"


	config = {
			'host':'localhost',
			'user':'root',
			'password':'1234',
			'database':'mydatabase'
		}

	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with the user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cursor = conn.cursor(dictionary=True)			#用這行產生字典型態撈資料比較好撈
		#cursor = conn.cursor()
		sql_query = ("SELECT * FROM inventory WHERE id = %s;")		#SQL語法
		cursor.execute(sql_query,(user_id,))						#執行SQL語法指令
		rows = cursor.fetchall()
		#print type(rows)								#PI顯示測試用
		#print rows										#PI顯示測試用
		data_string = json.dumps(rows)					#變數=把資料轉換成json格式指令
		#Cleanup
		cursor.close()
		conn.close()
		#return 'select ok'								#網頁上顯示的資訊
		return data_string								#網頁上顯示的資訊
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')