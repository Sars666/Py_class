import codecs
import requests, os
from bs4 import BeautifulSoup
from lxml import etree
import re
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter
from pandas import DataFrame
import math
import time

import weatherCrawler
import DataAnalysis

mainurl = 'http://www.tianqihoubao.com'
url = 'http://www.tianqihoubao.com/lishi'
encoding = 'gbk'
head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                      ' AppleWebKit/605.1.15 (KHTML, like Gecko)'
                      ' Version/12.0.1 Safari/605.1.15',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',}
filename = 'WeatherHistory'
req, reqState = weatherCrawler.urlAnalysis(url, filename)
maxCityNum = 1

if reqState == 200:
    weatherCrawler.main(mainurl, reqState, req, maxCityNum, filename, encoding)
else:
    print(reqState)

xlsxFile = pd.ExcelFile('./WeatherHistory/北京.xlsx')#分析不同的excel需要不同的文件名
DataAnalysis.tempPlot(xlsxFile)
