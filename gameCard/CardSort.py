#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 17:34
# @Author  : Shark
# @Site    : 
# @File    : CardSort.py
# @Software: PyCharm
colorIntMap = {
    "方片":1,
    "梅花":2,
    "红桃":3,
    "黑桃":4,
}

colorSort = {
    "3":1, #红桃
    "1":2, #方片
    "2":3, #梅花
    "4":4, #黑桃
}


colorStrSort = {
    "红桃":4, #红桃
    "方块":3, #方片
    "梅花":2, #梅花
    "黑桃":1, #黑桃
}

valueIntMap = {
    "3":3, #3
    "4":4, #4
    "5":5, #5
    "6":6, #6
    "7":7, #6
    "8":8, #6
    "9":9, #6
    "10":10, #6
    "J":11, #6
    "Q":12, #6
    "K":13, #6
    "A":1, #6
    "2":2, #6
}

valueStrSort = {
    "3":1, #3
    "4":2, #4
    "5":3, #5
    "6":4, #6
    "7":5, #6
    "8":6, #6
    "9":7, #6
    "10":8, #6
    "J":9, #6
    "Q":10, #6
    "K":11, #6
    "A":12, #6
    "2":13, #6
}

valueSort = {
    "3":1, #3
    "4":2, #4
    "5":3, #5
    "6":4, #6
    "7":5, #6
    "8":6, #6
    "9":7, #6
    "10":8, #6
    "11":9, #6
    "12":10, #6
    "13":11, #6
    "1":12, #6
    "2":13, #6
}

byteMap = {
    0x11 : "方块A",0x12: "方块2", 0x13 : "方块3" ,0x14 : "方块4",0x15 : "方块5" ,0x16 : "方块6" ,0x17:"方块7" ,0x18 : "方块8",0x19 : "方块9",0x1a :"方块10",0x1b : "方块J",0x1c : "方块Q",0x1d :"方块K",
    0x21 : "梅花A",0x22: "梅花2", 0x23 : "梅花3" ,0x24 : "梅花4",0x25 : "梅花5" ,0x26 : "梅花6" ,0x27:"梅花7" ,0x28 : "梅花8",0x29 : "梅花9",0x2a :"梅花10",0x2b : "梅花J",0x2c : "梅花Q",0x2d :"梅花K",
    0x31 : "红桃A",0x32: "红桃2", 0x33 : "红桃3" ,0x34 : "红桃4",0x35 : "红桃5" ,0x36 : "红桃6" ,0x37:"红桃7" ,0x38 : "红桃8",0x39 : "红桃9",0x3a :"红桃10",0x3b : "红桃J",0x3c : "红桃Q",0x3d :"红桃K",
    0x41 : "黑桃A",0x42: "黑桃2", 0x43 : "黑桃3" ,0x44 : "黑桃4",0x45 : "黑桃5" ,0x46 : "黑桃6" ,0x47:"红桃7" ,0x48 : "黑桃8",0x49 : "黑桃9",0x4a :"黑桃10",0x4b : "黑桃J",0x4c : "黑桃Q",0x4d :"黑桃K",
    0x5e : "小王",0x5f :"大王",
}

cardStrMap = {
}

def init():
    for(k,v) in byteMap.items():
        cardStrMap[v] = k
    print(cardStrMap)

init()

# 返回牌的权重值
def buidleCardByteWeight():
    cardByteWeight = {}
    for (colorK,colorV) in colorStrSort.items():
        for (varK,varV) in valueStrSort.items():
            cardStr = colorK + varK
            cardByte = cardStrMap.get(cardStr)
            cardByteWeight[cardByte] = colorV + varV

    return  cardByteWeight

def getValueSort(var):
    value = var.value
    sortInt = valueSort.get(value)
    if sortInt == None:
        return value
    return sortInt


def getColorSort(var):
    color = var.color
    sortInt = colorSort.get(color)
    if sortInt == None:
        return color
    return sortInt


def getColorIntForStr(colorInt):
    for (k,v) in colorIntMap.items():
        if v == colorInt:
            return k


def getColorStrForInt(colorStr):
    return colorIntMap[colorStr]

def getValueIntForStr(valuent):
    for (k,v) in valueIntMap.items():
        if v == valuent:
            return k


def getValueStrForInt(valueStr):
    return colorIntMap[valueStr]