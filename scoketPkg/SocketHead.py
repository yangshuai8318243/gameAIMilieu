#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 11:20
# @Author  : Shark
# @Site    : 
# @File    : SocketHead.py
# @Software: PyCharm

import struct



class HeadBuild():
    __HEAD_RPC__ = "RPC"
    __HEAD_VAR__ = 1

    def __init__(self):
        super(HeadBuild,self).__init__()

    def build(self,byteDta):
        rpcData = bytes(self.__HEAD_RPC__, encoding='utf-8')

        lenData = struct.pack(">H", len(byteDta))
        vData = bytes([self.__HEAD_VAR__])
        headData = rpcData + vData + lenData
        reqSendData = headData + byteDta
        return reqSendData

    def unBuold(self,byteData):
        rpcData = byteData[:3]

        if rpcData != bytes(self.__HEAD_RPC__, encoding='utf-8'):
            print("数据结构错误", str(rpcData))
            return

        verData = byteData[3:4]
        lenData = byteData[4:6]
        bodyLen = struct.unpack('>H', lenData)[0]
        print("===数据长度=====>", bodyLen)

        reqBodyData = byteData[6:len(byteData)]
        if len(reqBodyData) == bodyLen:
            return reqBodyData
        else:
            print('数据异常')

