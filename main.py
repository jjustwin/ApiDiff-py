__author__ = 'tjw'

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests
import configparser as cparser
from json import loads
from config import setting
from lib.readexcel import ReadExcel
from lib.sendrequests import SendRequests
from lib.login import Login
from lib.writeexcel import WriteExcel
from lib.replaceRelevance import get_value, replace

# --------- 读取config.ini配置文件 ---------------
cf = cparser.ConfigParser()
cf.read(setting.TEST_CONFIG, encoding='UTF-8')
host_t = cf.get("server", "host_t")
host_d = cf.get("server", "host_d")

requests.packages.urllib3.disable_warnings()
testData = ReadExcel(setting.SOURCE_FILE, "Sheet1").read_data()
# host_t = 'https://tapi.shining3d.com'
# host_d = 'http://10.10.1.57:7080'
relvance_t = {}
relvance_d = {}


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

        token_t = Login().login(host1)
        token_d = Login().login(host2)
        if data["module"] in ['采集微服务']:
            token_t = token_d = ''
        re_t = SendRequests().sendRequests(self.s, token_t, host1, replace(data, relvance_t)).text
        re_d = SendRequests().sendRequests(self.s, token_d, host2, replace(data, relvance_d)).text

        if re_t.startswith("{") and re_d.startswith("{") and isinstance(loads(re_t), str):
            if loads(re_d.get("status") == "success"):
                relvance_t.update(get_value(re_t, data["relvance"]))
                relvance_d.update(get_value(re_d, data["relvance"]))
                if loads(re_t) == loads(re_d):
                    print("接口返回一致======================")
                    OK_data = "PASS"
                    # print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
                    WriteExcel(setting.TARGET_FILE_dental).write_data(rowNum + 1, OK_data, 'PASS')
                    return
        print(f"请注意, {data['API']} 接口在两套环境中不一致", )
        print(host1, "返回信息：%s" % re_t)
        print(host2, "返回信息：%s" % re_d)
        NOT_data = "FAIL"
        # print("用例测试结果:  {0}---->{1}".format(data['ID'], NOT_data))
        WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, NOT_data, re_t + re_d)


if __name__ == '__main__':
    APIDIFF = apiDiff()
    for d in testData:
        APIDIFF.test_api(host_t, host_d, d)
