#coding=gbk
import urllib    
import urllib2  
import cookielib  

cookie = cookielib.CookieJar()    
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  

#��ҪPOST������#  
postdata=urllib.urlencode({    
    'name':'M201276020',     
    'password':'206144kevin'    
})  

#�Զ���һ������#  
req = urllib2.Request(    
    url = 'http://myself.hust.edu.cn:8080/selfservice/module/scgroup/web/login_judge.jsf',
    data = postdata  
)  

req2 = urllib2.Request(url = 'http://myself.hust.edu.cn:8080/selfservice/module/webcontent/web/index_self_hk.jsf')

#���ʸ�����#  
opener.open(req)      #�ȵ�¼
result = opener.open(req2)

#��ӡcookie��ֵ  
for item in cookie:    
    print 'Cookie��Name = '+item.name    
    print 'Cookie��Value = '+item.value 

#��ӡ���ص�����#  
#print result.read()
#print result.read()

#���ʸ�����#  
result = opener.open('http://myself.hust.edu.cn:8080/selfservice/module/userself/web/regpassuserinfo_update_hk.jsf')
print result.read()  