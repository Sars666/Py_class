import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter
from pandas import DataFrame
import math, os
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname='PingFang', size=12)


# 月份坐标轴
def month_formatter(x, pos):
    v = int(x / 31) + 1
    if v > 12:
        return '-'
    else:
        return str(v)


# hsv转rgb
def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1:
        r, g, b = q, v, p
    elif hi == 2:
        r, g, b = p, v, t
    elif hi == 3:
        r, g, b = p, q, v
    elif hi == 4:
        r, g, b = t, p, v
    elif hi == 5:
        r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


# rgb转16#
def color(value):
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, tuple):
        string = '#'
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        return string


def tempGridSetting():
    plt.gca().xaxis.set_major_locator(MultipleLocator(31))
    plt.gca().xaxis.set_major_formatter(FuncFormatter(month_formatter))
    plt.setp(plt.gca().get_xticklabels(), horizontalalignment='center')
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, y: str(x) + 'C°'))
    plt.gca().grid()


def weatherStata(WeatherList):
    weatherDic = {}
    for weather in WeatherList:
        if weather in weatherDic.keys():
            weatherDic[weather] += 1
        else:
            weatherDic[weather] = 1
    return weatherDic


def tempPlot(xlsxFile):
    # 初始化
    avgTemp = []
    lowestTemperature = []
    highestTemperature = []
    dateTime = []
    amWeatherList = []
    pmWeatherList = []
    windStrenthList = []
    sheetNameList = xlsxFile.sheet_names

    df_TAVG = DataFrame(columns=['datetime', 'temp', 'color'])  # 平均气温数据
    df_THIG = DataFrame(columns=['datetime', 'temp', 'color'])  # 最高气温数据
    df_TLOW = DataFrame(columns=['datetime', 'temp', 'color'])  # 最低气温数据
    df_TD = DataFrame(columns=['datetime', 'temp', 'color'])  # 最低气温数据
    df_AWEA = DataFrame(columns=['datetime', 'weather'])  # 上午气象数据
    df_PWEA = DataFrame(columns=['datetime', 'weather'])  # 下午气象数据

    print(len(sheetNameList))

    # 存入各个数据及其对应日期
    for sheetName in range(len(sheetNameList)):
        currentSheet = xlsxFile.parse(sheetNameList[sheetName])
        for row in range(currentSheet.iloc[:, 0].size):
            dateTime.append(currentSheet.iloc[[row]].values[0][0])

            amWeatherList.append(currentSheet.iloc[[row]].values[0][1])
            pmWeatherList.append((currentSheet.iloc[[row]].values[0][2])[1:])

            highestTemperature.append(int((currentSheet.iloc[[row]].values[0][3])[:-1]))
            lowestTemperature.append(int((currentSheet.iloc[[row]].values[0][5])[:-1]))

            windStrenthList.append((currentSheet.iloc[[row]].values[0][6])[-4:-1])

    # 计算平均气温 and 将相关数据存入DataFrame
    for i in range(len(lowestTemperature)):
        aT = (lowestTemperature[i] + highestTemperature[i]) / 2
        avgTemp.append(aT)

        # 平均气温TAVG
        _color = color(tuple(hsv2rgb(int(-7 * aT) + 240, 1, 1)))  # 设置数据颜色值
        _df = DataFrame({'datetime': [dateTime[i]], 'dayIndex': [(i + 1) % 365],
                         'temp': [aT], 'color': [_color]})
        df_TAVG = df_TAVG.append(_df, ignore_index=True)

        # 最高气温HAVG
        _color = color(tuple(hsv2rgb(int(-7 * highestTemperature[i]) + 240, 1, 1)))
        _df = DataFrame({'datetime': [dateTime[i]], 'dayIndex': [(i + 1) % 365],
                         'temp': [highestTemperature[i]], 'color': [_color]})
        df_THIG = df_THIG.append(_df, ignore_index=True)

        # 最低气温LAVG
        _color = color(tuple(hsv2rgb(int(-7 * lowestTemperature[i]) + 240, 1, 1)))
        _df = DataFrame({'datetime': [dateTime[i]], 'dayIndex': [(i + 1) % 365],
                         'temp': [lowestTemperature[i]], 'color': [_color]})
        df_TLOW = df_TLOW.append(_df, ignore_index=True)

        # 温差TD
        _color = color(tuple(hsv2rgb(int(-7 * (highestTemperature[i] - lowestTemperature[i])) + 240, 1, 1)))
        _df = DataFrame({'datetime': [dateTime[i]], 'dayIndex': [i % 365],
                         'temp': [highestTemperature[i] - lowestTemperature[i]], 'color': [_color]})
        df_TD = df_TD.append(_df, ignore_index=True)

        # 上午天气AWEA
        _df = DataFrame({'datetime': [dateTime[i]], 'dayIndex': [(i + 1) % 365],
                         'weather': [amWeatherList[i]]})
        df_AWEA = df_AWEA.append(_df, ignore_index=True)

        # 下午天气PWEA
        _df = DataFrame({'datetime': [dateTime[i]], 'dayIndex': [(i + 1) % 365],
                         'weather': [pmWeatherList[i]]})
        df_PWEA = df_PWEA.append(_df, ignore_index=True)

    df_TAVG = df_TAVG.set_index('datetime')
    df_THIG = df_THIG.set_index('datetime')
    df_TLOW = df_TLOW.set_index('datetime')
    df_TD = df_TD.set_index('datetime')

    #
    if not os.path.isdir('./pic'):
        os.mkdir('./pic')
    # 最高最低温度散点图
    tempGridSetting()
    plt.figure(figsize=(12, 9))
    plt.scatter(df_TLOW['dayIndex'], df_TLOW['temp'],
                c='mediumpurple', marker='o', alpha=0.05)
    plt.scatter(df_THIG['dayIndex'], df_THIG['temp'],
                c='red', marker='o', alpha=0.05)
    plt.ylim(-30, 50)
    plt.title('TempCurve : 2011-2019')
    plt.xlabel("Month")
    plt.ylabel("Temperature C°")
    plt.legend()
    plt.savefig("./pic/HighLowTemp.png", bbox_inches='tight')  # 保存图片
    plt.show()

    # 绘制平均温度散点图
    plt.figure(figsize=(12, 9))
    plt.subplot(2, 2, 1)
    tempGridSetting()
    plt.scatter(df_TAVG['dayIndex'], df_TAVG['temp'], s=80,
                c=df_TAVG['color'], marker='o', alpha=0.05)
    plt.ylim(-30, 50)
    plt.title('avgTemp : 2011-2019')
    plt.xlabel("Month")
    plt.ylabel("Temperature C°")

    # 绘制最高温度散点图
    plt.subplot(2, 2, 2)
    tempGridSetting()
    plt.scatter(df_THIG['dayIndex'], df_THIG['temp'], s=80,
                c=df_THIG['color'], marker='o', alpha=0.05)
    plt.ylim(-30, 50)
    plt.title('higTemp : 2011-2019')
    plt.xlabel("Month")
    plt.ylabel("Temperature C°")

    # 绘制最低温度散点图
    plt.subplot(2, 2, 3)
    tempGridSetting()
    plt.scatter(df_TLOW['dayIndex'], df_TLOW['temp'], s=80,
                c=df_TLOW['color'], marker='o', alpha=0.05)
    plt.ylim(-30, 50)
    plt.title('lowTemp : 2011-2019')
    plt.xlabel("Month")
    plt.ylabel("Temperature C°")

    # 绘制温度差异散点图
    plt.subplot(2, 2, 4)
    tempGridSetting()
    plt.scatter(df_TD['dayIndex'], df_TD['temp'], s=80,
                c=df_TD['color'], marker='o', alpha=0.05)
    plt.ylim(-30, 50)
    plt.title('TD : 2011-2019')
    plt.xlabel("Month")
    plt.ylabel("Temperature C°")
    plt.savefig("./pic/Temp.png", bbox_inches='tight')  # 保存图片
    plt.show()

    # 绘制气象情况条形图
    amWeatherDic = weatherStata(df_AWEA['weather'])
    pmWeatherDic = weatherStata(df_PWEA['weather'])
    aList = sorted(amWeatherDic, key=amWeatherDic.__getitem__, reverse=True)
    pList = sorted(pmWeatherDic, key=pmWeatherDic.__getitem__, reverse=True)
    aValue = []
    pValue = []
    for key in aList:
        aValue.append(amWeatherDic[key])
    for key in pList:
        pValue.append(pmWeatherDic[key])

    plt.figure(figsize=(12, 9))
    plt.subplot(2, 1, 1)
    font_set = FontProperties(fname="simsun.ttc", size=12)
    plt.setp(plt.gca().get_xticklabels(), horizontalalignment='center')
    plt.xticks(range(len(aList)), aList, FontProperties=font_set, rotation=60)
    plt.bar(aList, aValue)
    plt.ylim(0, 1300)

    plt.subplot(2, 1, 2)
    plt.setp(plt.gca().get_xticklabels(), horizontalalignment='center')
    plt.xticks(range(len(aList)), aList, FontProperties=font_set, rotation=60)
    plt.bar(pList, pValue)
    plt.ylim(0, 1300)
    plt.savefig("./pic/Weather.png", bbox_inches='tight')
    plt.show()

    print('Saved')
