__author__ = 'tjw'

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests
from json import loads
from config import setting
from lib.readexcel import ReadExcel
from lib.sendrequests import SendRequests
from lib.login import Login
from lib.writeexcel import WriteExcel

requests.packages.urllib3.disable_warnings()
testData = ReadExcel(setting.SOURCE_FILE, "Sheet1").read_data()
host_t = 'https://t.dental3dcloud.com/api'
host_d = 'http://10.10.1.57:7080'


class apiDiff():
    """API比较脚本"""

    s = requests.session()

    def test_api(self, host1, host2, data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[2])
        print("******* 正在执行接口 ->{0} *********".format(data['ID']))
        # print("请求方式: {0}，请求URL: {1}".format(data['method'], data['host1']))
        print("请求参数: {0}".format(data['params']))
        # 发送请求

        cookie1 = Login().login(host1)
        cookie2 = Login().login_dev(host2)
        if data["module"] in ['采集微服务']:
            cookie1 = cookie2 = {}
        re1 = SendRequests().sendRequests(self.s, cookie1, host1, data).text
        re2 = SendRequests().sendRequests(self.s, cookie2, host2, data).text
        if re1.startswith("{") and re2.startswith("{"):
            if loads(re1) == loads(re2) and loads(re1).get("status","fail") == "success":
                print("接口返回一致======================")
                OK_data = "PASS"
                # print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
                WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, OK_data, 'PASS')
                return
        print(f"请注意, {data['API']} 接口在两套环境中不一致", )
        print(host1, "返回信息：%s" % re1)
        print(host2, "返回信息：%s" % re2)
        NOT_data = "FAIL"
        # print("用例测试结果:  {0}---->{1}".format(data['ID'], NOT_data))
        WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, NOT_data, re1 + re2)


if __name__ == '__main__':
    APIDIFF = apiDiff()
    for d in testData:
        APIDIFF.test_api(host_t, host_d, d)
