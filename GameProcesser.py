#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:53
# @Author  : Shark
# @Site    : 
# @File    : GameProcesser.py
# @Software: PyCharm

from pb import base_pb2
from scoketPkg.EventManager import EventTag

import json

class Processer():
    GAME_ID = 21
    LEVEL = 3
    LEVEL_TYPE = 1
    PLAY_TYPE = "normal"
    ALLOC_NAME = "alloc.Alloc"
    GAME_SCOKET_NAME = "gameser.OnGameMsg"
    GAME_VERSION = 9999


    def __init__(self,user,hallSocket):
        self.__userData = user
        self.__hallSocket = hallSocket
        self.__hallSocket.addEven(self.ALLOC_NAME,self.allocListener)
        self.__hallSocket.addEven(self.GAME_SCOKET_NAME,self.onGameMsgListener)


    def buildGameData(self,funName,clientPbmsg):
        gameMsgReq = base_pb2.GameMsgReq()
        gameMsgReq.uid = self.__userData.uid
        gameMsgReq.method = 'gameser.'+funName
        gameMsgReq.pb_format = funName
        gameMsgReq.client_pbmsg = clientPbmsg
        return gameMsgReq.SerializeToString()

    def sendAlloc(self):
        sendData = self.buildAlloc()

        self.__hallSocket.sendMsg(self.ALLOC_NAME,sendData)

    def allocListener(self,evenData):
        body = evenData.getData("body")
        rpc_code = evenData.getData("rpc_code")
        if rpc_code != 0 :
            print("rpc 错误 ：",rpc_code)
        else:
            allocData = self.unBuildAlloc(body)
            if allocData.err_code != 0 :
                print("子游戏配桌错误 ：",allocData.err_code)
            else:
                print("-allocListener--->",allocData)

    def onGameMsgListener(self,evenData):
        print(evenData)

        body = evenData.getData("body")
        rpc_code = evenData.getData("rpc_code")

        if body != None and body != "" and rpc_code == 0 :
            gameMsgResp = base_pb2.GameMsgResp()
            gameMsgResp.ParseFromString(body)
            method = gameMsgResp.method
            client_pbmsg = gameMsgResp.client_pbmsg
            uid = gameMsgResp.uid

            event = EventTag(type_=method)
            event.dict["method"] = method
            event.dict["body"] = client_pbmsg
            event.dict["uid"] = uid
            
            self.__hallSocket.getEvenManager().SendEvent(event)


    def sendGameMsg(self,method,gameData):

        gameMsgReq = base_pb2.GameMsgReq()
        gameMsgReq.uid = self.__userData.uid
        gameMsgReq.method = method
        gameMsgReq.pb_format = "game." + method
        gameMsgReq.client_pbmsg = gameData

        sendData = gameMsgReq.SerializeToString()

        self.__hallSocket.sendMsg(self.GAME_SCOKET_NAME,sendData)

    def buildAlloc(self):
        allocReq = base_pb2.AllocReq()
        allocReq.uid = self.__userData.uid
        allocReq.info = ""
        allocReq.client_ip = self.__hallSocket.get_host_ip()
        allocReq.gameid = self.GAME_ID
        allocReq.level = self.LEVEL
        allocReq.levelType = self.LEVEL_TYPE
        allocReq.playType = self.PLAY_TYPE
        jsonData = {
            "nick" : self.__userData.nick,
            "sex" : self.__userData.sex,
            "uid" : self.__userData.uid,
            "version" : self.GAME_VERSION,
        }

        jsonDataStr = json.dumps(jsonData)

        allocReq.info = jsonDataStr

        byteData = allocReq.SerializeToString()

        return byteData

    def unBuildAlloc(self,body):
        allocResp = base_pb2.AllocResp()
        allocResp.ParseFromString(body)
        return  allocResp
