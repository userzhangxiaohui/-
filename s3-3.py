import urllib.request
from http.cookiejar import CookieJar
#获取cookie
url = 'http://www.zhihu.com'
cookie = CookieJar()
response = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie)).open(url)
for item in cookie:
    print(item.name + ':' + item.value)