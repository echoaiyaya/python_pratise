import requests
import time
from bs4 import BeautifulSoup

headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'accept-encoding':'gzip, deflate, br',
           'accept-language':'zh-CN,zh;q=0.9',
           'cache-control':'max-age=0',
           'referer':'https://www.biquge.com.cn/book/33556/',
           'upgrade-insecure-requests':'1',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
html = requests.get('https://www.biquge.com.cn/book/28334/', headers=headers)
html.encoding = 'gb2312'
bsObj = BeautifulSoup(html.text)
catelists = []
# print(bsObj)
catelisthtmls = bsObj.find('div',{'id':'list'}).findAll('a')
for catelisthtml in catelisthtmls:
    catelists.append(catelisthtml['href'])
# print(catelists)
for catelist in catelists:
    content = requests.get('https://www.biquge.com.cn' + catelist, headers=headers)
    content.encoding = 'utf-8'
    cbsObj = BeautifulSoup(content.text)
    titlehtml = cbsObj.find('div', {'class':'bookname'}).h1
    titleName = titlehtml.get_text()
    print(titleName)
    contenthtmls = str(cbsObj.find('div', {'id': 'content'}))
    pcontent = contenthtmls.replace(r'<div id="content">', '')
    pcontent = pcontent.replace(r'</div>', '')
    pcontent = pcontent.replace(r'<br/><br/>', '\r')
   
    with open('老衲要还俗.txt', 'a', encoding="utf-8") as f:
            f.write('章节名:'+titleName+'\r\n')
            f.write(pcontent+'\r\n')
            f.write('====================================================================\r\n\r\n')
    time.sleep(0.5)