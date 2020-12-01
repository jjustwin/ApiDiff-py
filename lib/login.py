#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/26 16:22
# @Author : jayveet
# @Site : 
# @File : login.py
# @Software: PyCharm
import requests, json
host_t = 'https://t.dental3dcloud.com'
host_d = 'http://10.10.1.57:7080'


class Login():
    s = requests.session()
    method = 'post'
    api = '/api/login'
    api_dev = '/login'
    global cookie
    cookie = "uuid=20c75426-2034-49ff-a688-fef30cd1914b; cc=CN; lang=zh-cn; oemURL=index; country=CN"
    headers = '{"cookie":"uuid=20c75426-2034-49ff-a688-fef30cd1914b; cc=CN; lang=zh-cn; oemURL=index; country=CN"}'
    h = json.loads(headers)
    h_dev = h
    h_dev['X-Auth-AppId'] = '2d274d917e32a1188f39ba102bc378da'
    body_data = {"loginType": "dental-cloud", "username": "victor@shining3d.com", "password": "111111", "rPwd": False,
                 "phoneArea": "86"}
    body = json.dumps(body_data)

    def login(self, host):
        # print(self.body)
        re = self.s.request(method=self.method, url=host + self.api, headers=self.h, data=self.body)
        global cookie
        token = re.json()['result']['token']
        UTitle = re.json()['result']['nick_name']
        user_id = re.json()['result']['user_id']
        # new_cookie = cookie + "; token=" + token + "; token=" + user_id
        new_cookie = cookie + "; token=" + token + "; token=" + user_id + "; UTitle=" + UTitle

        return new_cookie.encode('utf-8')

    def login_dev(self, host):
        # print(self.body)
        re = self.s.request(method=self.method, url=host + self.api_dev, headers=self.h_dev, data=self.body)
        global cookie
        if re.text.startswith("{"):
            token = re.json()['result']['Token']
            UTitle = re.json()['result']['NickName']
            user_id = re.json()['result']['UserID']
            # new_cookie = cookie + "; token=" + token + "; token=" + user_id
            new_cookie = cookie + "; token=" + token + "; token=" + user_id + "; UTitle=" + UTitle
        else:
            return {}

        return new_cookie.encode('utf-8')
    # return re.json()['result']['token']


if __name__ == '__main__':
    cookie_t = Login().login(host_t)
    cookie_d = Login().login_dev(host_d)
    print("The cookie of env_t is : %s" % cookie_t)
    print("The cookie of env_t is : %s" % cookie_d)
