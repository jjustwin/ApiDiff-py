#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os, sys, json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class SendRequests():
    """发送请求数据"""

    def sendRequests(self, s, apiData):
        try:
            # 从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url1 = apiData["host1"]
            url2 = apiData["host2"]
            api = apiData["API"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"].replace("false", "False"))
            type = apiData["type"]
            v = False
            # v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data
            # re = s.request(method=method, url=url, headers=h, params=par, data=body, verify=v)
            # return re
            # 发送请求
            try:
                re1 = s.request(method=method, url=url1 + api, headers=h, params=par, data=body, verify=v)
            except Exception as e:
                print(e, url1 + api, "请求失败")
            try:
                re2 = s.request(method=method, url=url2 + api, headers=h, params=par, data=body, verify=v)
            except Exception as e:
                print(e, url2 + api, "请求失败")
            return re1, re2
        except Exception as e:
            print(e)
