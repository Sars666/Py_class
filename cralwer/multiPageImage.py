import codecs
import requests,os
import re
from bs4 import BeautifulSoup
from lxml import etree

#创建空文件夹
def createEmptyDir(targetDir):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
#保存图片并命名
def savePhotoFromUrl(url,name,number,head):
    targetDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'multiPageImage')
    createEmptyDir(targetDir)
    t = os.path.join(targetDir+'/'+name+'/'+str(number+1)+'.jpg')#文件命名
    createEmptyDir(targetDir+'/'+name+'/')
    fw = open(t,'wb')
    r = requests.get(url,headers=head)
    fw.write(r.content)
    fw.close()
    print(name+'---'+str(number+1)+'.jpg '+'downloaded')

#网页基本参数
url = 'https://www.meitulu.com/rihan/'
encoding = 'utf-8'
head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                              ' AppleWebKit/605.1.15 (KHTML, like Gecko)'
                              ' Version/12.0.1 Safari/605.1.15',
                         "Referer": "https://www.meitulu.com/item/17517.html",
                         "Accept": "text/css,*/*;q=0.1"}

#获取url并用BS4分析
def urlAnalysis(url):
    req = requests.get(url)
    req.encoding =encoding
    reqState =req.status_code
    return req,reqState

def saveHtml(req):
    soup = BeautifulSoup(req.text,features="lxml")
    with codecs.open("multiPageImage.html", "w", "utf-8") as f:
        f.write(soup.prettify())
    return soup

#用etree得到图片地址和标题
def getHrefAndTitle(req):
    xmlContent = etree.HTML(req.text)
    hrefList = xmlContent.xpath("//ul[@class='img']/li/a/@href")
    titleList = xmlContent.xpath("//ul[@class='img']/li/a/img/@alt")
    return hrefList,titleList

#由图片地址下载图片
def downloadImg(hrefList,titleList):
    for setNumber in range(len(hrefList)):
        newReq = requests.get(hrefList[setNumber])
        xmlContent = etree.HTML(newReq.text)
        imgUrlList = xmlContent.xpath("//div[@class='content']/center/img/@src")
        currentPageNumber = xmlContent.xpath("//div[@id='pages']/span")
        maxImgNumber = int(re.findall('\\[(\\d*)\\]',titleList[setNumber])[0])
        for currentImgNumber in range(maxImgNumber):
            currentImgUrl = imgUrlList[0][0:-6]+'/'+str(currentImgNumber) + '.jpg'
            savePhotoFromUrl(url=currentImgUrl,name=titleList[setNumber],number=currentImgNumber,head=head)
        print('saved')


def main():
    if reqState == 200:
        print('Url Request Accepted')
        soup = saveHtml(req)
        hrefList,titleList = getHrefAndTitle(req)
        downloadImg(hrefList,titleList)
    else:
        print('Url Request Denied')

req,reqState = urlAnalysis(url)
main()