#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os, sys, json
from uuid import uuid1

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class SendRequests():
    """发送请求数据"""

    def sendRequests(self, s, token, host, apiData):
        try:
            # 从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = host
            # url2 = apiData["host2"]
            api = apiData["API"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            if apiData["headers"] == "":
                h = {}
                h['X-Auth-Token'] = token
                h['X-Auth-AppId'] = '2d274d917e32a1188f39ba102bc378da'

            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"].replace("false", "False").replace("true", "True"))
                if "fingerprint" in body_data:
                    body_data["fingerprint"] = str(uuid1())
            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
                h.update({"content-type": "application/json"})
            else:
                body = body_data
            # re = s.request(method=method, url=url, headers=h, params=par, data=body, verify=v)
            # return re
            # 发送请求
            re = {}
            if ":" in api:
                # 设定val,从par或者body取值
                val = par if par else body if body else {}
                # 根据/:分割出key
                api_back = api.split("/:")[1:]
                # 遍历,从val中取值替换
                for key in api_back:
                    url = url.replace(key, val.get(key, ""), 1)
            url = url + api
            try:
                print(f"请求body内容为：{method}  {url}  {h}  {par}")
                re = s.request(method=method, url=url, headers=h, params=par, data=body, verify=v)
            except Exception as e:
                print(e, url + api, "请求失败")
            return re
        except Exception as e:
            print(e)
