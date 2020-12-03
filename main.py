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
# 关系网ID
tid = ''
# 机构ID
targetID = ''
userID = ''

# host_t = 'https://tapi.shining3d.com'
# host_d = 'http://10.10.1.57:7080'
relvance_t = {}
relvance_d = {}


class apiDiff():
    """API比较脚本"""

    s = requests.session()

    def test_api(self, host1, host2, token_t, token_d, data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        try:
            rowNum = int(data['ID'].split("_")[2])
        except Exception as e:
            print(e)

        print("******* 正在请求第{0}个接口->:{1} API_URL->:{2} *********".format(rowNum, data['UseCase'], data['API']))
        # print("请求方式: {0}，请求URL: {1}".format(data['method'], data['host1']))
        # print("请求参数: {0}".format(data['params']))
        # 发送请求

        # token_t = Login().login(host1)
        # token_d = Login().login(host2)
        if data["module"] in ['采集微服务']:
            token_t = token_d = ''
        print("******* 正在请求测试环境接口 *********")

        re_t = SendRequests().sendRequests(self.s, token_t, host1, data).text


        print("******* 正在请求开发环境接口 *********")
        re_t = SendRequests().sendRequests(self.s, token_t, host1, replace(data, relvance_t)).text
        re_d = SendRequests().sendRequests(self.s, token_d, host2, replace(data, relvance_d)).text

        if re_t.startswith("{") and re_d.startswith("{") and isinstance(loads(re_t), str):
            if loads(re_d.get("status") == "success"):
                relvance_t.update(get_value(re_t, data["relvance"]))
                relvance_d.update(get_value(re_d, data["relvance"]))
                if loads(re_t) == loads(re_d):
                    print("接口返回一致======================")
                    OK_data = "PASS"
                    print("******* 正在请求第{0}个接口请求完成*********\n".format(rowNum))
                    # print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
                    WriteExcel(setting.TARGET_FILE_dental).write_data(rowNum + 1, OK_data, 'PASS')
                    return 'Pass'
        print(host1, "返回信息：%s" % re_t)
        print(host2, "返回信息：%s" % re_d)
        print(f"请注意, {data['API']} 接口在两套环境中不一致", )
        print("******* 第{0}个接口请求完成*********\n".format(rowNum))
        NOT_data = "FAIL"
        # print("用例测试结果:  {0}---->{1}".format(data['ID'], NOT_data))
        WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, NOT_data, re_t, re_d)
        return 'FAIL'


if __name__ == '__main__':
    APIDIFF = apiDiff()
    token_t = Login().login(host_t)
    token_d = Login().login(host_d)
    sum_pass = 0
    sum_fail = 0
    for d in testData[0:1]:
        result = APIDIFF.test_api(host_t, host_d, token_t, token_d, d)
        if result == 'PASS':
            sum_pass = sum_pass + 1
        else:
            sum_fail = sum_fail + 1
    print("本次共请求{0}个接口，接口响应一致的{1}个，接口响应不一致的{2}个".format(sum_pass + sum_fail, sum_pass, sum_fail))
    # APIDIFF.test_api(host_t, host_d, token_t, token_d, testData[32])
