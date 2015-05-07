#coding=gbk
import urllib
import urllib2
import cookielib
import re

class HUST_Spider:
    #声明相关属性
    def __init__(self):
        self.loginUrl = 'http://myself.hust.edu.cn:8080/selfservice/module/scgroup/web/login_judge.jsf'
        self.indexUrl = 'http://myself.hust.edu.cn:8080/selfservice/module/webcontent/web/index_self_hk.jsf'
        self.resultUrl = 'http://myself.hust.edu.cn:8080/selfservice/module/userself/web/regpassuserinfo_update_hk.jsf'
        self.cookieJar = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'name':'M201276020',
            'password':'206144kevin'            
    })
        self.info = []
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))
     
    def hust_init(self):
        #初始化链接并且获取cookie
        myRequest = urllib2.Request(url = self.loginUrl, data = self.postdata)
        result = self.opener.open(myRequest)
        result = self.opener.open(self.indexUrl)
        result = self.opener.open(self.resultUrl)
        #打印返回的内容
        #print result.read()
        page = result.read().decode('gbk')
        self.deal_data(page)
    
    #将内容从页面中取出来
    def deal_data(self, mypage):
        r = r'RegUserinfoForm.*>(.*)</span></span>'
        myItem = re.findall(r,mypage)
        for item in myItem:
            self.info.append(item[0].encode('gbk'))
        print myItem
#调用          
mySpider = HUST_Spider()
mySpider.hust_init()
    
