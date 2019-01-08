#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/loginurl', methods=['GET', 'POST'])
def login1():
	if request.method == 'POST':
		return redirect(url_for('hello', username2=request.form.get('username1')))
		#如果收到HTML傳來的POST,導向到def hello 頁面 ,username1是HTML傳過來的資料

	return render_template('login.html')	#http://192.168.XX.XX:5000/loginurl顯示login.html網頁

@app.route('/hello/<username2>')
def hello(username2):
	return render_template('hello.html', username5=username2)

@app.route('/')                    #http://192.168.XX.XX:5000/
def index():                       #首頁function
	return "Hello world"           #顯示Hello

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0') 