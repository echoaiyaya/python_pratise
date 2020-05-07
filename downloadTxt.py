import requests
import time
from bs4 import BeautifulSoup

path = r'G:\网盘资源\pratise\《少年的你如此美丽》.txt'
headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'accept-encoding':'gzip, deflate, br',
           'accept-language':'zh-CN,zh;q=0.9',
           'cache-control':'max-age=0',
           'cookie':'__cfduid=d647d4c118fac764af87e15f97e639e071554376802; Hm_lvt_249365e1d51157c1854dd9425bb4e860=1554376814; Hm_lpvt_249365e1d51157c1854dd9425bb4e860=1554378553',
           'if-modified-since':'Fri, 22 Mar 2019 02:06:07 GMT',
           'referer':'https://www.qishulou.com/yanqing/shaonian/522097.html',
           'upgrade-insecure-requests':'1',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
html = requests.get('https://www.qishulou.com/yanqing/shaonian/', headers=headers)
html.encoding = 'gb2312'
bsObj = BeautifulSoup(html.text)
catelists = []
print(bsObj)
return
catelisthtmls = bsObj.find('div',{'class':'book-list'}).findAll('a')
for catelisthtml in catelisthtmls:
    catelists.append(catelisthtml['href'])
print(catelists)
for catelist in catelists:
    content = requests.get(catelist, headers=headers)
    content.encoding = 'utf-8'
    cbsObj = BeautifulSoup(content.text)
    titlehtml = cbsObj.find('', {'class':'post-header'}).h1
    titleName = titlehtml.get_text()
    print(titleName)
    contenthtmls = cbsObj.findAll('p')
    pcontent = ''
    for p in contenthtmls:
          pcontent = pcontent + p.get_text() + '\r\n\r\n'
    with open(path, 'a', encoding="utf-8") as f:
            f.write('章节名:'+titleName+'\r\n')
            f.write(pcontent+'\r\n')
            f.write('====================================================================\r\n\r\n')
    time.sleep(0.5)