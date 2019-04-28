import codecs
import requests,os
from bs4 import BeautifulSoup
from lxml import etree

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
    hrefList = xmlContent.xpath('//*[@id="container"]/ol/li/div[3]/div[@class="icon_img"]/a/@href')
    return hrefList

#由图片地址下载图片
def downloadImg(hrefList,maxSetNumber):
    if hrefList != [] :
        for setNumber in range(len(hrefList)):
            if maxSetNumber > 0:
                moreUrl = mainurl+hrefList[setNumber]
                moreReq = urlAnalysis(moreUrl)[0]
                moreXmlContent = etree.HTML(moreReq.text)
                setName = moreXmlContent.xpath('/html/body/div[2]/div[2]/div[3]/dl/dd[2]/a/text()')[0]
                moreHref = moreXmlContent.xpath('//*[@id="container"]/ol/li[21]/a/@href')
                currentSetUrl = mainurl + moreHref[0]
                currentSetReq = requests.get(currentSetUrl)
                currentSetXmlContent = etree.HTML(currentSetReq.text)
                iconUrlList = currentSetXmlContent.xpath('//*[@id="container"]/ol/li/div[3]/div/a/img/@src')
                iconNameList = currentSetXmlContent.xpath('//*[@id="container"]/ol/li/div[3]/div/a/img/@alt')
                for currentIconNumber in range(len(iconNameList)):
                    currentIconUrl = iconUrlList[currentIconNumber]
                    savePhotoFromUrl(url=currentIconUrl,setName=setName,iconName=iconNameList[currentIconNumber]
                                     ,number=currentIconNumber,head=head)
                space = ' '* (60-len(setName))
                print(setName+ space+'saved')
                maxSetNumber -= 1
    else:
        print('Invalid Keyword!')

#创建空文件夹
def createEmptyDir(targetDir):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
#保存图片并命名
def savePhotoFromUrl(url,setName,iconName,number,head):
    targetDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),filename)
    createEmptyDir(targetDir)
    t = os.path.join(targetDir+'/'+setName+'/'+iconName+'.jpg')#文件命名
    createEmptyDir(targetDir+'/'+setName+'/')
    fw = open(t,'wb')
    r = requests.get(url)
    fw.write(r.content)
    fw.close()
    iconNameInDir = setName+'---'+iconName+'.jpg '
    space = ' '* (50-len(iconNameInDir))
    print(iconNameInDir+space+'downloaded')

#主程序
def main():
    if reqState == 200:
        print('Url Request Accepted')
        saveHtml(req)
        hrefList = getHref(req)
        downloadImg(hrefList,maxSetNumber)
    else:
        print('Url Request Denied')


#输入关键词,然后在页面搜索相关icon并下载同一系列所有icon
#输入所需要的icon系列数,默认20
maxSetNumber = 24
keyword = '火'
mainurl = 'https://www.easyicon.net/'
url = f'https://www.easyicon.net/iconsearch/{keyword}/?s=addtime_DESC'
encoding = 'utf-8'
head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                              ' AppleWebKit/605.1.15 (KHTML, like Gecko)'
                              ' Version/12.0.1 Safari/605.1.15'}
filename = 'multiPageIcon'
req,reqState = urlAnalysis(url)
main()