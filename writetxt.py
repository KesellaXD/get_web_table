#coding:utf-8
import os
fileName=os.getcwd()+'table.txt'
strg='你好'
f=open('table.txt',"w")
f.write(strg)
f.close()
