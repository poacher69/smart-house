#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask, render_template	#載入網頁製作套件, 網頁指向套件
from flask import request, url_for			#載入POST,GET套件

import mysql.connector
from mysql.connector import errorcode
import json									#載入json套件
import time	,datetime				#載入時間套件

app = Flask(__name__)

@app.route('/')
def index():
	ip = request.remote_addr
    return render_template('index.html' , user_ip=ip)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')