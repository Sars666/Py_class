import codecs
import requests,os
from bs4 import BeautifulSoup
from lxml import etree
import shutil

#获取url并用BS4分析
def urlAnalysis(url):
    req = requests.get(url)
    req.encoding =encoding
    reqState =req.status_code
    return req,reqState

#用BS4保存Html文件
def saveHtml(req):
    soup = BeautifulSoup(req.text,features="lxml")
    with codecs.open(filename+".html", "w", "utf-8") as f:
        f.write(soup.prettify())
    return soup

#用etree得到图片地址和标题
def getHref(req):
    xmlContent = etree.HTML(req.text)
    hrefList = xmlContent.xpath('//*[@id="container"]/ol/li/div[@class="pd_img"]/div[@class="icon_img"]/a/@href')
    return hrefList

def getMaxIconNum(url):
    req = urlAnalysis(url)[0]
    xmlContent = etree.HTML(req.text)
    maxIcon = xmlContent.xpath('//*[@id="nav_left_layout"]/div[@class="total_icons"]/span/text()')
    return maxIcon[0]

#由图片地址下载图片
def downloadImg(hrefList):
    targetDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),filename)
    if os._exists(targetDir):
        shutil.rmtree(targetDir)
    if hrefList != [] :
        id = 1
        for hrefNumber in range(len(hrefList)):
            imgReq = urlAnalysis(mainurl+hrefList[hrefNumber])[0]
            imgXmlContent = etree.HTML(imgReq.text)
            imgHref = imgXmlContent.xpath('/html/body/div[2]/div[2]/div[1]/div/a/img/@src')
            imgUrl = mainurl + imgHref[0]
            imgName = imgXmlContent.xpath('/html/body/div[2]/div[2]/div[1]/div/a/img/@alt')
            savePhotoFromUrl(url=imgUrl,iconName=imgName,head=head,id=id)
            id+=1
    else:
        print('Cannot Find Any Icon Related')

#创建空文件夹
def createEmptyDir(targetDir):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)

#保存图片并命名
def savePhotoFromUrl(url,iconName,head,id):
    targetDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),filename)
    createEmptyDir(targetDir)
    t = os.path.join(targetDir+'/'+str(id)+' '+iconName[0]+'.png')#文件命名
    createEmptyDir(targetDir+'/')
    fw = open(t,'wb')
    r = requests.get(url)
    fw.write(r.content)
    fw.close()
    print(t)

#主程序
def main():
    if reqState == 200:
        print('Url Request Accepted')
        saveHtml(req)
        hrefList = getHref(req)
        downloadImg(hrefList)
    else:
        print('Url Request Denied')


#输入关键词,然后在页面搜索相关icon并下载同一系列所有icon
#输入最大页数?

keyword = 'icon'
mainurl = 'https://www.easyicon.net/'
encoding = 'utf-8'
head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                              ' AppleWebKit/605.1.15 (KHTML, like Gecko)'
                              ' Version/12.0.1 Safari/605.1.15'}
filename = 'SearchResult'

pageNum = 1
url = f'https://www.easyicon.net/iconsearch/{keyword}/s=addtime_DESC'
maxIconNum = getMaxIconNum(url)
maxPage = int(int(maxIconNum.replace(',','')) / 50) +1
for pageNum in range(maxPage):
    pageNum +=1
    url = f'https://www.easyicon.net/iconsearch/{keyword}/{pageNum}/?m=yes&f=_all&s=addtime_DESC'
    req,reqState = urlAnalysis(url)
    main()
