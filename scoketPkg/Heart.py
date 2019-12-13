#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 18:39
# @Author  : Shark
# @Site    : 
# @File    : Heart.py
# @Software: PyCharm
from threading import *
from pb import heart_pb2

class Heart():
    __RPC_NAME__ = "heartbeat.common"

    def __init__(self,socketHall):
        self.token = ""
        self.socketHall = socketHall
        self.count = 0
        self.socketHall.addEven(self.__RPC_NAME__,self.heartListener)

    def getRpcName(self):
        return self.__RPC_NAME__

    def buildHeartData(self):
        heartData = heart_pb2.HeartReq()
        heartData.heart = ""

        return heartData.SerializeToString()

    def unBuildHeartData(self,bodyData):
        heartData = heart_pb2.HeartResp()
        heartData.ParseFromString(bodyData)
        return heartData

    def sendHeart(self):
        heartData = self.buildHeartData()
        # print("---------sendHeart-->",heartData)
        self.count += 1
        self.socketHall.sendMsg(self.__RPC_NAME__,heartData)
        print("=====self.count====>",self.count)
        self.startHeart()

    def heartListener(self,evenData):
        bodyData = evenData.dict["body"]
        if bodyData != None and bodyData != "":

            heartData = self.unBuildHeartData(bodyData)
            if heartData != None and heartData.token != None:
                self.token = heartData.token
                self.socketHall.setToken(self.token)

    def startHeart(self):
        timer = Timer(3, self.sendHeart)
        timer.start()
