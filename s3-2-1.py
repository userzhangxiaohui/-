import urllib.request
import urllib

url = 'http://www.zhihu.com'
response = urllib.request.urlopen(url)
html = response.read(50)
print(html)