#-*- coding:utf-8 -*-

import requests
import re

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

headers1= ({
    'Referer': 'http://www.pixiv.net/',
    'User-Agent': user_agent
})

def getid():
	url1 = 'http://www.pixiv.net/ranking.php?mode=daily'#每日排行榜
	res1 = requests.get(url1,headers=headers1)

	print res1.headers

	content1 = res1.text.encode('utf-8')
	pattern1 = re.compile('(?<=data-id=")\S*(?=">)')
	dataids = re.findall(pattern1, content1)  # 寻找id
	if not dataids:
	    print 'getids is error'
	    exit()
	    # 判断是否成功
	print 'getids is Success'
	return dataids

getid()