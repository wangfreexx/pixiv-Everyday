#-*- coding:utf-8 -*-

import requests
import re
import os
import time
import m.cookie
import m.saveimg
import m.getids


pid = ''  # 账号
password = ''  # 密码
number = 5  # 下载图片数量
ceiling=4#防止下载到漫画，每个id图片上限
ctext = '/mnt/p/'+'cookie.txt'  # cookie位置
add='/mnt/p/img'#linux绝对地址
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 获取系统时间
mkpath = str(today)

filename = ctext
if os.path.exists(filename):
    cookies = m.cookie.loadcookie(ctext)
else:
    while pid=='' and password=='':
                pid=raw_input("Please enter your account number:")
                password=raw_input("Please input a password：")
    m.cookie.getcookies(pid=pid, password=password,text=ctext)
    cookies = m.cookie.loadcookie(ctext)  # 读取cookie


dataids=m.getids.getid()
saveimg.mkdir(add)#创建img文件夹
saveimg.mkdir(add+'/'+mkpath)#创建日期文件夹
mkpath=add+'/'+mkpath
m.saveimg.save(Number=number,dataids=dataids,text=ctext,cookies=cookies,path=mkpath)

