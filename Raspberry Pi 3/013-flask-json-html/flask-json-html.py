#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def result():
   dict = {'phy':'2018/10/14','che':60,'maths':70}
   return render_template('main.html', result = dict)
  
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)