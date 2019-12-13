#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 10:55
# @Author  : Shark
# @Site    : 
# @File    : SocketHall.py
# @Software: PyCharm
from socket import *
from .import SocketHead
from .import Heart
from pb import socket_pb2

from threading import *
from scoketPkg.EventManager import *


class HallScoket():
    __HOST__ = "vietnam.oa.com"
    __POST__ = 9010
    __SIZE__ = (1024 * 5)

    def __init__(self):
        self.__scokeHead = SocketHead.HeadBuild()
        self.token = ""

        self.__buildSocket()
        self.__eventManager = EventManager()
        self.__eventManager.Start()

        self.__heart = Heart.Heart(self)

        self.__thread = Thread(target=self.waitMsg).start()

    def getEvenManager(self):
        return  self.__eventManager
    def get_host_ip(self):
        """
        查询本机ip地址
        :return: ip
        """
        ip = ""
        if self.__tcpClientSocket :
            ip = self.__tcpClientSocket.getsockname()[0]
        return ip

    def startHeart(self):
        print()
        self.__heart.startHeart()

    def setToken(self, token):
        print("更新 token newToken ->",token," odeToken ->",self.token)
        self.token = token

    def __buildSocket(self):
        ADDR = (self.__HOST__, self.__POST__)
        self.__tcpClientSocket = socket(AF_INET, SOCK_STREAM)
        self.__tcpClientSocket.connect(ADDR)

    def addEven(self,rpcName,fun):
        self.__eventManager.AddEventListener(rpcName, fun)

    def sendMsg(self,rpcName,body):
        scoketData = self.buildRpcData(body,rpcName)
        sendData = self.__scokeHead.build(scoketData)
        self.__tcpClientSocket.send(sendData)

    def waitMsg(self):
        try:
            while True:
                reqData = self.__tcpClientSocket.recv(self.__SIZE__)
                if reqData != None:
                    rpcData = self.__scokeHead.unBuold(reqData)
                    socketData = self.unBuildRpcData(rpcData)

                    rpcName = socketData.rpc
                    event = EventTag(type_=rpcName)
                    event.dict["rpc"] =  rpcName
                    event.dict["body"] =  socketData.body
                    event.dict["token"] =  socketData.token
                    event.dict["rpc_code"] =  socketData.code
                    print("-----waitMsg---->", socketData)
                    if socketData.token:
                        self.setToken(socketData.token)

                    if socketData.body :
                        lock = Lock()
                        with lock:
                            self.__eventManager.SendEvent(event)
        except Exception as e:
            print(e)

    def buildRpcData(self,byteData,rpcName):

        socketData = socket_pb2.RpcReq()
        socketData.rpc = rpcName
        socketData.ext = ""
        socketData.token = self.token
        socketData.body = byteData
        print("-----buildRpcData---->", socketData)
        return socketData.SerializeToString()

    def unBuildRpcData(self, byteData):
        socketData = socket_pb2.RpcRsp()
        socketData.ParseFromString(byteData)
        return socketData



