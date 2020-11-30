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
    global cookie
    cookie = "uuid=20c75426-2034-49ff-a688-fef30cd1914b; cc=CN; lang=zh-cn; oemURL=index; country=CN"
    headers = '{"cookie":"uuid=20c75426-2034-49ff-a688-fef30cd1914b; cc=CN; lang=zh-cn; oemURL=index; country=CN"}'
    h = json.loads(headers)
    body_data = {"loginType": "dental-cloud", "username": "13300000041", "password": "888888", "rPwd": False,
                 "phoneArea": "86"}
    body = json.dumps(body_data)

    # @classmethod
    def login(self, host):
        # print(self.body)
        re = self.s.request(method=self.method, url=host + self.api, headers=self.h, data=self.body)
        global cookie
        token = re.json()['result']['token']
        UTitle = re.json()['result']['nick_name']
        user_id = re.json()['result']['user_id']
        new_cookie = cookie + "; token=" + token + "; token=" + user_id + "; UTitle=" + UTitle

        return new_cookie

        # return re.json()['result']['token']


if __name__ == '__main__':
    cookie = Login().login('https://t.dental3dcloud.com')
    print("The cookie is : %s" % cookie)
