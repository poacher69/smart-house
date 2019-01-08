#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask, render_template	#載入網頁製作套件, 網頁指向套件
from flask import request, url_for			#載入POST,GET套件
app = Flask(__name__)

@app.route('/para/<user>')
def index(user):
    return render_template('abc.html', user_template=user)

if __name__ == '__main__':
    app.debut = True
    app.run()