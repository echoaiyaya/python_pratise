import requests
import warnings
import time
from bs4 import BeautifulSoup
warnings.filterwarnings('ignore')


headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'accept-encoding':'gzip, deflate, br',
           'accept-language':'zh-CN,zh;q=0.9',
           'cache-control':'max-age=0',
           'referer':'https://www.biquge.com.cn/book/38825/',
           'upgrade-insecure-requests':'1',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
results = []

def linkTimeout(url, time):
    while True:
        try:
            html = requests.get(url, headers=headers, timeout=int(time))
            return html
        except:
            print('请求响应超时3秒，重新请求')
    

def download(num):
    book = results[int(num)-1]
    html = linkTimeout('https://www.biquge.com.cn' + book["href"], 3)
    html.encoding = 'gb2312'
    bsObj = BeautifulSoup(html.text)
    catelists = []
    # print(bsObj)
    catelisthtmls = bsObj.find('div',{'id':'list'}).findAll('a')
    for catelisthtml in catelisthtmls:
        catelists.append(catelisthtml['href'])
    index = 1
    for catelist in catelists:
        content = linkTimeout('https://www.biquge.com.cn' + catelist, 3)
        content.encoding = 'utf-8'
        cbsObj = BeautifulSoup(content.text)
        titlehtml = cbsObj.find('div', {'class':'bookname'}).h1
        titleName = titlehtml.get_text()
        print(titleName)
        contenthtmls = str(cbsObj.find('div', {'id': 'content'}))
        pcontent = contenthtmls.replace(r'<div id="content">', '')
        pcontent = pcontent.replace(r'</div>', '')
        pcontent = pcontent.replace(r'<br/><br/>', '\r\n')
       
        with open( book["name"] + '.txt', 'a', encoding="utf-8") as f:
                f.write('第'+ str(index) +'章节 章节名:'+titleName+'\r\n')
                f.write(pcontent+'\r\n')
                f.write('====================================================================\r\n\r\n')
        time.sleep(0.1)
        index += 1

def showResult():
    i = 1 
    if results == []:
        print("无结果,请重新输入，或是输入0退出")
    else:
        for result in results:
            print(str(i) + ": " + result["name"])
            print(result["content"])
            print('================================')
            i += 1

def search(name):
    searchUrl = 'https://www.biquge.com.cn/search.php?q=' + name
    html = linkTimeout(searchUrl, 3)
    bsObj = BeautifulSoup(html.text)
    htmlPrints = bsObj.findAll("div", {"class":"result-game-item"})
    results.clear()
    for htmlPrint in htmlPrints:
        book = {}
        bookTitle = htmlPrint.find('a', {"class", "result-game-item-title-link"})
        book['name'] = bookTitle['title']
        book['href'] = bookTitle['href']
        book['content'] = htmlPrint.find('div', {"class": "result-game-item-info"}).get_text().replace('\n', ' ')
        
        results.append(book)
    showResult()

def getName():
    span = True
    while span:
        name = input("请输入小说名：")
        search(name)
        num = input("请输入序列号(输入e退出)(输入r重新搜索)：")
        if num == 'e':
            exit()
        elif num == 'r':
            span = True
        else:
          span = False
    return num


if __name__ == '__main__':

    num = getName()
    download(num)


