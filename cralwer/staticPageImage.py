import codecs
import requests,os
import re
from bs4 import BeautifulSoup

#由Url爬网页
def getUrl(url):
    req = requests.get(url)
    req.encoding = encoding
    return req

#得到请求状态--200为正常
def reqState(req):
    code = req.status_code
    # print(code)
    return code

#BeautifulSoup美化并存储html文件
def saveHtml(req):
    soup = BeautifulSoup(req.text,features="lxml")
    with codecs.open("staticPageImage.html", "w", "utf-8") as f:
        f.write(soup.prettify())
    return soup

#利用BS4找到所有关键标签的内容
def findElement(keyLabel):
    html = soup.find_all(keyLabel)
    # print(html)
    elementList = []
    for i in range(len(html)):
        elementList +=(html[i])
    return elementList

#正则匹配得到地址等的列表
def crawlList(reg):
    crawlList= []
    for i in range(len(elementList)):
        crawlList += re.findall(reg, str(elementList[i]))
    # print(crawlList)
    return crawlList

def getUrlList(crawlList):
    imageAddressList = []
    for i in range(len(crawlList)):
        imageAddressList.append(url+crawlList[i])
    # print(imageAddressList)
    return imageAddressList


#保存图片
def savePhoto():
    for i in range(len(imageAddressList)):
        targetDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'staticPageImage')
        if not os.path.isdir(targetDir):
            os.mkdir(targetDir)
        t = os.path.join(targetDir+'/'+nameList[i]+'.jpg')#文件命名
        fw = open(t,'wb')
        r = requests.get(imageAddressList[i])
        fw.write(r.content)
        fw.close()
    print('saved')


url = 'http://pic.netbian.com'
encoding = 'gbk'

req = getUrl(url)
reqState =reqState(req)

if reqState == 200:
    print('Url Request Accepted')
    soup = saveHtml(req)
    keyLabel = 'span'
    elementList = findElement(keyLabel)
    imageReg = "src=\"([.*\S]*\.jpg)"
    nameReg = "img alt=\"([.*\S\s]*)\"[\s src=]"
    nameList = crawlList(nameReg)
    imageList = crawlList(imageReg)
    imageAddressList = getUrlList(imageList)
    savePhoto()
else:
    print('Url Request Denied')
