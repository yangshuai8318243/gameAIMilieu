#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 15:50
# @Author  : Shark
# @Site    : 
# @File    : card.py
# @Software: PyCharm

byteMap = {
    0x11 : "方块A",0x12: "方块2", 0x13 : "方块3" ,0x14 : "方块4",0x15 : "方块5" ,0x16 : "方块6" ,0x17:"方块7" ,0x18 : "方块8",0x19 : "方块9",0x1a :"方块10",0x1b : "方块J",0x1c : "方块Q",0x1d :"方块K",
    0x21 : "梅花A",0x22: "梅花2", 0x23 : "梅花3" ,0x24 : "梅花4",0x25 : "梅花5" ,0x26 : "梅花6" ,0x27:"梅花7" ,0x28 : "梅花8",0x29 : "梅花9",0x2a :"梅花10",0x2b : "梅花J",0x2c : "梅花Q",0x2d :"梅花K",
    0x31 : "红桃A",0x32: "红桃2", 0x33 : "红桃3" ,0x34 : "红桃4",0x35 : "红桃5" ,0x36 : "红桃6" ,0x37:"红桃7" ,0x38 : "红桃8",0x39 : "红桃9",0x3a :"红桃10",0x3b : "红桃J",0x3c : "红桃Q",0x3d :"红桃K",
    0x41 : "黑桃A",0x42: "黑桃2", 0x43 : "黑桃3" ,0x44 : "黑桃4",0x45 : "黑桃5" ,0x46 : "黑桃6" ,0x47:"红桃7" ,0x48 : "黑桃8",0x49 : "黑桃9",0x4a :"黑桃10",0x4b : "黑桃J",0x4c : "黑桃Q",0x4d :"黑桃K",
    0x5e : "小王",0x5f :"大王",
}

ColorMap = {
	1 : "方块",
	2 : "梅花",
	3 : "红桃",
	4 : "黑桃",
	5 : "王",
}

ValueMap = {
	1 : "A",
	2 : "2",
	3 : "3",
	4 : "4",
	5 : "5",
	6 : "6",
	7 : "7",
	8 : "8",
	9 : "9",
	10 : "10",
	11 : "J",
	12 : "Q",
	13 : "K",
	14 : "小王",
	15 : "大王",
}


class CardData():
    def __init__(self,byteData):
        self.byteData = byteData
        self.color , self.value,self.colorStr , self.valueStr = self.getByteForCardData(byteData)

    def getByteForCardData(self,byteData):
        byte2 = byteData % 0x100
        print("byte2:", byte2)
        color = int(byte2 / 0x10)
        value = byte2 % 0x10
        colorStr = ColorMap[color]
        valueStr = ValueMap[value]

        return color , value,colorStr , valueStr


    def __repr__(self):
        return str(self.colorStr) + str(self.valueStr)


