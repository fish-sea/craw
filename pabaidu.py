#!/usr/bin/env python
#coding=utf-8

import re
import urllib2
from bs4 import BeautifulSoup as bs

"""爬取百度首页的图片
                   """

url='http://image.baidu.com/'
web=urllib2.urlopen(url)
buf=web.read()

soup=bs(buf,'html.parser')
#print soup
lib=soup.findAll('img',src=re.compile('^http'))
#print lib
x=0
for val in lib:
	#print val['src']
	f=open('baidu'+str(x)+'.jpg','w')
	fi=urllib2.urlopen(val['src'])
	wen=fi.read()
	print '正在保存%d幅图片......' %(x+1)
	f.write(wen)
	print '第%d幅图片保存成功' %(x+1)
	f.close()
	x+=1
print 'Completed!!'
