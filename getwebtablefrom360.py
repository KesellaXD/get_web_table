#coding:utf-8
import requests
import gzip
from bs4 import BeautifulSoup
import datetime
import os
import openpyxl
from lxml import etree


today1 = datetime.date.today()
yesterday1 = today1 - datetime.timedelta(days=1)
today2 = str(today1)
yesterday = str(yesterday1)


url = "http://chart.cp.360.cn/kaijiang/kaijiang?lotId=255401&spanType=2&span="+today2+"_"+today2
r=requests.get(url)
data=r.text
data=etree.HTML(data)
data=etree.tostring(data)
data = data.decode('GBK','strict')
soup= BeautifulSoup(data,"html.parser")
#print(soup)
dict={}
tbodys=soup.find_all('tbody')
for i in range(0,3):
    trs=tbodys[i].find_all('tr')
    for tr in trs:
        #print(tr)
        try:
            win_number=tr.find('td',class_='red big').string[0:1]+' '+tr.find('td',class_='red big').string[1:2]+' '+tr.find('td',class_='red big').string[2:3]+' '+tr.find('td',class_='red big').string[3:4]+' '+tr.find('td',class_='red big').string[4:5]
        except:
            win_number=None
        try:
            tr.find('td',class_='gray').string
        except:
            continue
        if dict.__contains__(today2[2:4]+today2[5:7]+today2[8:10]+tr.find('td',class_='gray').string):
            continue
        else:
            dict.get(today2[2:4]+today2[5:7]+today2[8:10]+tr.find('td',class_='gray').string)
            dict[today2[2:4]+today2[5:7]+today2[8:10]+tr.find('td',class_='gray').string]=win_number


