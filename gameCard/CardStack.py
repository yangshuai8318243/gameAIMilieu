#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 15:15
# @Author  : Shark
# @Site    : 
# @File    : CardStack.py
# @Software: PyCharm
import numpy as np
from .import card


# 矩阵举例
#     代表      数量   A   2   3   4   5   6   7   8   9   10   J    Q    K   小王 大王
# 	             [0]  [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15]
# 	数量 [0]      52   4   4   4   4   4   4   4   4   4   4    4    4    4    1    1
# 	方片 [1]      13   1   1   1   1   1   1   1   1   1   1    1    1    1    0    0
# 	梅花 [2]      13   1   1   1   1   1   1   1   1   1   1    1    1    1    0    0
# 	红桃 [3]      13   1   1   1   1   1   1   1   1   1   1    1    1    1    0    0
# 	黑桃 [4]      13   1   1   1   1   1   1   1   1   1   1    1    1    1    0    0
# 	王牌 [5]      2    0   0   0   0   0   0   0   0   0   0    0    0    0    1    1



class CardStackData():
    def __init__(self,myCards):
        self.myBytesCards = myCards
        self.myCards = self.__buildeCards(myCards)
        self.cardMatrix = np.zeros((6,16))
        self.__initMatrix()

    def __initMatrix(self):
        for item in self.myCards:
            var = item.value
            color = item.color
            self.cardMatrix[0,0] = self.cardMatrix[0,0] + 1
            self.cardMatrix[color,var] = self.cardMatrix[color,var] + 1
            self.cardMatrix[color,0] = self.cardMatrix[color,0] +1
            self.cardMatrix[0, var] = self.cardMatrix[0,var] +1


    def __buildeCards(self,bytes):
        cards = []
        for item in bytes:
            cardObj = card.CardData(item)
            cards.append(cardObj)
        return  cards



    def getValueList(self,sortFun = None):
        varList = []
        for item in  self.myCards:
            varList.append(item)
        if sortFun != None:
            varList.sort(key=sortFun)
        return  varList

    def getColorList(self,sortFun = None):
        varList = []
        for item in self.myCards:
            varList.append(item)
        if sortFun != None:
            varList.sort(key=sortFun)
        return varList

    def getValueMap(self):
        mapData = {

        }
        for item in self.myCards :
            value = item.value
            mapKeyData = mapData.get(value)
            if mapKeyData == None :
                mapKeyData = []
            mapKeyData.append(item)
            mapData[value] = mapKeyData

        return mapData

    def getColorMap(self):
        mapData = {

        }
        for item in self.myCards:
            color = item.color
            mapKeyData = mapData.get(color)
            if mapKeyData == None:
                mapKeyData = []
            mapKeyData.append(item)
            mapData[color] = mapKeyData

        return mapData


    def __repr__(self):
        return str(self.cardMatrix)