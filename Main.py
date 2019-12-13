#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 18:59
# @Author  : Shark
# @Site    : 
# @File    : Main.py
# @Software: PyCharm

from Login import *

from scoketPkg.SocketHall import *
from gameCard.CardStack import *

from GameProcesser import Processer


class MainObj:

    def __init__(self):
        self.login = Login(self)
        self.hallScoket = HallScoket()
        self.hallScoket.addEven(self.login.getRpcName(),self.login.loginListener)


    def loginFun(self,token):
        print("=====Main====login==>")
        self.hallScoket.startHeart()
        self.gameProcesser = Processer(hallSocket = self.hallScoket,user = self.login.getUserData())
        self.gameProcesser.sendAlloc()

    def start(self):
        print("-------sendMsg------>")
        # self.hallScoket.startHeart()
        loginData = self.login.budilLogin()
        loginRpcName = self.login.getRpcName()
        self.hallScoket.sendMsg(loginRpcName,loginData)

    def test(self):
        cardSobj = CardStackData(myCards = [0x11,0x12,0x13,0x31])

        print(cardSobj.getColorList())
        print(cardSobj.__class__.__name__)
def run():
    maObj = MainObj()
    # maObj.start()
    maObj.test()


if __name__ == '__main__':
    run()