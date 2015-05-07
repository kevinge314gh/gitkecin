#coding = 'gbk'
import urllib
import urllib2
import re

class ChouBai_Spider:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
    
    #�����еĶ���ȡ����
    def GetPage(self, page):
        myUrl = 'http://m.qiushibaike.com/hot/page/' + page
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent' : user_agent}
        req = urllib2.Request(myUrl, headers = headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        
        #�ҳ�����class="content"��div���
        r = r'<div.*?class="content".*?title="(.*?)">(.*?)</div>'
        myItem = re.findall(r, myPage, re.S)
        items = []
        for item in myItem:
            items.append(item[0].replace('\n', ''),item[1].replace('\n', ''))
        return items
    
    def ShowPage(self):
        
        