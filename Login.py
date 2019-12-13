#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 19:10
# @Author  : Shark
# @Site    : 
# @File    : Login.py
# @Software: PyCharm

from pb import login_pb2


class Login():
    __RPC_NAME__ = "login.Login"


    def __init__(self,mainObj):
        self.__mainObj = mainObj

    def getRpcName(self):
        return self.__RPC_NAME__

    def unBudilLogin(self,body):
        loginDataPb = login_pb2.LoginResp()
        loginDataPb.ParseFromString(body)
        return loginDataPb

    def loginListener(self,evenData):
        bodyData = evenData.dict["body"]
        loginData = self.unBudilLogin(bodyData)
        # print("==loginListener====>",loginData)
        if loginData != None :
            uid = loginData.data.uid
            nick = str(loginData.user.nick)
            icon = str(loginData.user.icon)
            sex = loginData.user.sex
            money = loginData.user.money
            coin = loginData.user.coin
            self.__userData = UserData(uid,nick,icon,sex,money,coin)
            self.__mainObj.loginFun(loginData.data.token)
    def getUserData(self):
        return self.__userData

    def budilLogin(self):
        loginData = login_pb2.LoginReq()
        loginData.appid = 1
        loginData.account = "321"
        loginData.oldAccount = ""
        loginData.login_type = 1
        loginData.apk_ver = "1.5.0"
        loginData.hall_ver = 150
        loginData.channel_id = 1
        loginData.param = '{"token":""}'
        loginData.device_type = 0
        loginData.lang = "vi"
        byteData = loginData.SerializeToString()

        return byteData

class UserData:
    def __init__(self,uid,nick,icon,sex,money,coin):
        self.uid = uid
        self.nick = nick
        self.icon = icon
        self.sex = sex
        self.money = money
        self.coin = coin

    def __str__(self):
        return "uid:" + str(self.uid) + "\nnick:" + self.nick + "\nicon:" + self.icon + "\nsex:" + str(self.sex) + "\nmoney:" \
               + str(self.money) + "\ncoin:" + str(self.coin)
