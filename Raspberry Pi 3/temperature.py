#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time,datetime                #載入時間套件

from time import strftime           #從time套件載入strftime套件

temperature = file("temp.txt","w")  #建立文字檔案，用以儲存時間跟溫度資料

for num in range(5):
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
  temperature.write(str(now)+"          "+str(temp))  #資料寫入到temp.txt
  temperature.write("\n")                             #資料寫入到temp.txt換行
  time.sleep(1)
temperature.close     #file關閉
  
  
  