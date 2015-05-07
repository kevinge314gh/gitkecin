#coding=gbk
import urllib    
import urllib2  
import cookielib  

cookie = cookielib.CookieJar()    
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  

#需要POST的数据#  
postdata=urllib.urlencode({    
    'name':'M201276020',     
    'password':'206144kevin'    
})  

#自定义一个请求#  
req = urllib2.Request(    
    url = 'http://myself.hust.edu.cn:8080/selfservice/module/scgroup/web/login_judge.jsf',
    data = postdata  
)  

req2 = urllib2.Request(url = 'http://myself.hust.edu.cn:8080/selfservice/module/webcontent/web/index_self_hk.jsf')

#访问该链接#  
opener.open(req)      #先登录
result = opener.open(req2)

#打印cookie的值  
for item in cookie:    
    print 'Cookie：Name = '+item.name    
    print 'Cookie：Value = '+item.value 

#打印返回的内容#  
#print result.read()
#print result.read()

#访问该链接#  
result = opener.open('http://myself.hust.edu.cn:8080/selfservice/module/userself/web/regpassuserinfo_update_hk.jsf')
print result.read()  