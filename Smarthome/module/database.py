#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
from mysql.connector import errorcode
import json

##################建立Database類別的function###################################
class Database:								#定義類別名稱
	def connect(self):						#定義Mysql連線方法
		# Obtain connection string information from the portal
		config = {
		'host':'localhost',
		'user':'root',
		'password':'1234',
		'database':'mydatabase'
		}
		
		# Construct connection string
		try:
			print("Connection established")
			return mysql.connector.connect(**config)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with the user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)


	def execute(self,sql_query,parameter):		#定義方法
		print "execute."
		conn = Database.connect(self)
		cursor = conn.cursor()
		cursor.execute(sql_query,parameter)
		conn.commit()

		cursor.close()
		conn.close()

	def execute_select(self,sql_query):			#定義方法
		print "execute_select."
		conn = Database.connect(self)
		cursor = conn.cursor(dictionary=True)	#用這行產生字典型態撈資料比較好撈
		try:
			cursor.execute(sql_query)
			rows = cursor.fetchall()
			cursor.close()
			conn.close()
			#data_string = json.dumps(rows)		#變數=把資料轉換成json格式指令
			return rows
		except:
			conn.close()
			return "error"