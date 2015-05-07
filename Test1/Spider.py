#coding=gbk
import urllib
import urllib2
import cookielib
import re

class HUST_Spider:
    #�����������
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
        #��ʼ�����Ӳ��һ�ȡcookie
        myRequest = urllib2.Request(url = self.loginUrl, data = self.postdata)
        result = self.opener.open(myRequest)
        result = self.opener.open(self.indexUrl)
        result = self.opener.open(self.resultUrl)
        #��ӡ���ص�����
        #print result.read()
        page = result.read().decode('gbk')
        self.deal_data(page)
    
    #�����ݴ�ҳ����ȡ����
    def deal_data(self, mypage):
        r = r'RegUserinfoForm.*>(.*)</span></span>'
        myItem = re.findall(r,mypage)
        for item in myItem:
            self.info.append(item[0].encode('gbk'))
        print myItem
#����          
mySpider = HUST_Spider()
mySpider.hust_init()
    
