#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, request		#載入網頁製作套件,POST,GET套件
app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])			#網頁使用GET,POST方法
def login():
	if request.method == 'POST': 
		return 'Hello ' + request.values['username']
	return "<form method='post' action='/login'><input type='text' name='username' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')