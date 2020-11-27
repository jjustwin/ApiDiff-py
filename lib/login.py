#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/26 16:22
# @Author : jayveet
# @Site : 
# @File : login.py
# @Software: PyCharm
import requests, json

class Login():
    s = requests.session()
    method = 'post'
    api = '/api/login'
    headers = '{"cookie":"uuid=20c75426-2034-49ff-a688-fef30cd1914b; cc=CN; lang=zh-cn; oemURL=index; country=CN"}'
    h = json.loads(headers)
    body_data = {"loginType":"dental-cloud","username":"13300000041","password":"888888","rPwd":False,"phoneArea":"86"}
    body = json.dumps(body_data)
    # @classmethod
    def login(self, host):
        print(self.body)
        re = self.s.request(method=self.method, url=host + self.api, headers=self.h, data=self.body, verify=False)

        return re

if __name__ == '__main__':
    r = Login().login('https://t.dental3dcloud.com')
    print(r.json()['result']['token'])

    print ("end")

