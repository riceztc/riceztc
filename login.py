'''
该代码利用selenium库模拟浏览器打开相关网页进行手工登录获得cookie，利用cookie通过request模块再次进行登录。
'''





from selenium import webdriver
import time
from urllib import request
from http import cookiejar

driver = webdriver.Chrome()
driver.get("https://weibo.com/riceztc?wvr=4&lf=reg&is_all=1#_loginLayer_1512219458590") 
time.sleep(20)
cookiesD = driver.get_cookies()
cookie = []
for item in cookiesD:
    cookie1 = item["name"] + "=" + item["value"]
    cookie.append(cookie1)
cookiestr = ';'.join(cookie) 
curpage_url = driver.current_url
header={    
    "Cookie":cookiestr,
    }
req = request.Request(curpage_url,headers=header)
r = request.urlopen(req)
print(r.read().decode('utf-8'))
driver.quit()


