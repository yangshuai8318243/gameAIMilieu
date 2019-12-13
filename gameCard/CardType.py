#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 18:17
# @Author  : Shark
# @Site    : 
# @File    : CardType.py
# @Software: PyCharm
import numpy as np
from .import CardStack
from .import CardSort

shunZiSeriesWeight = {
    "1" : "3",
    "2" : "4",
    "3" : "5",
    "4" : "6",
    "5" : "7",
    "6" : "8",
    "7" : "9",
    "8" : "10",
    "9" : "J",
    "10" : "Q",
    "11" : "K",
    "12" : "A",
}

shunZiMaxSize = 12


class CardTypeData():
    def __init__(self,myCards):
        self.myCards = CardStack.CardStackData(myCards)
        self.cardByteWeight = CardSort.buidleCardByteWeight()

    def isCardStack(self,obj):
        if obj.__class__.name == "CardStackData" :
            return True
        return False

    def getShunzi(self,targetCards):
        if self.isCardStack(targetCards):
            print("不是牌堆")
            return False
        targetVarList = targetCards.getValueList(sortFun=CardSort.getValueSort)
        targetSize = len(targetVarList)

        if targetSize <3 :
            print("牌型长度错误")
            return False

        targetMinCard = targetVarList[0]

        selfCardSize = len(self.myCards.getValueList(sortFun=CardSort.getValueSort))
        if selfCardSize < targetSize :
            print("目标牌型过长")
            return False

        myValueMap = self.myCards.getValueMap()


        for( key , seriesWeight) in shunZiSeriesWeight.items():
            numKey = int(key)
            num = 0
            shunZi = []

            #判断当前连牌数字是否满足目标最小value
            if numKey == targetMinCard.value :
                numList = myValueMap[numKey]

                #当前连牌的value在当前手牌中是否有牌
                if len(numList) <= 0 :
                    continue

                numList.sort(key=CardSort.getColorSort)
                numMaxCard = numList[len(numList)-1]

                #当前连牌的值，在当前手牌中通过花色排序，最大花色是否比目标最小牌的花色大
                if CardSort.colorSort[str(numMaxCard.color)] < CardSort.colorSort[str(targetMinCard.color)]:
                    continue
                shunZi.append(numMaxCard)


                num = + 1
                for i in range(targetSize+1):
                    index = numKey + i
                    var = shunZiSeriesWeight.get(str(index))
                    #查找连牌是否存在
                    if var == None:
                        shunZi.clear()
                        break

                    varInt = int(var)
                    varCont = self.myCards.cardMatrix[0,varInt]

                    if varCont <= 0 :
                        continue

                    varList = myValueMap[varInt]
                    varList.sort(key=CardSort.getColorSort)
                    intCard = varList[0]
                    shunZi.append(intCard)
                    num = + 1
                    if num == targetSize :
                        break

            #判断连牌的值大于目标的最小牌值
            elif numKey > targetMinCard.value:
                numKeyList = myValueMap.get(numKey)
                #判断当前连牌的牌值在手牌中是否存在
                if len(numKeyList) <=0:
                    continue
                numKeyList.sort(key=CardSort.getColorSort)
                minMyIntCard = numKeyList[0]
                shunZi.append(minMyIntCard)
                num =+ 1





        print()

    def getDanPai(self,targetCards):
        print()

    def getDuizi(self,targetCards):
        print()

    def getSanzhuang(self,targetCards):
        print()

    def getSizhang(self,targetCards):
        print()