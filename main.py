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
        global isSame
        isSame = ''
        print("******* 正在请求第{0}个接口->:{1} API_URL->:{2} *********".format(rowNum, data['UseCase'], data['API']))
        #采集微服务不需要token
        if data["module"] in ['采集微服务']:
            token_t = token_d = ''
        print("******* 正在请求测试环境接口 *********")
        re_t = SendRequests().sendRequests(self.s, token_t, host1, replace(data, relvance_t)).text
        print("******* 正在请求开发环境接口 *********")
        re_d = SendRequests().sendRequests(self.s, token_d, host2, replace(data, relvance_d)).text
        if re_t == re_d:
            isSame = 'PASS'
            print("***********************接口返回一致*******************")
        else:
            isSame = 'FAIL'
            print(f"请注意, {data['API']} 接口在两套环境中不一致")
        print(host1, "返回信息：%s" % re_t)
        print(host2, "返回信息：%s" % re_d)
        print("******* 第{0}个接口请求完成*********".format(rowNum))
        print("=======================================================================================\n")
        #excel中如果包含替换字段则取值赋给变量
        if data["relvance"] != "":
            if re_t.startswith("{"):
                relvance_t.update(get_value(re_t, eval(data["relvance"])))
            if re_d.startswith("{"):
                relvance_d.update(get_value(re_d, eval(data["relvance"])))

        WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, isSame, re_t, re_d)
        return isSame

if __name__ == '__main__':
    APIDIFF = apiDiff()
    token_t = Login().login(host_t)
    token_d = Login().login(host_d)
    sum_pass = 0
    sum_fail = 0
    for d in testData[:]:
        result = APIDIFF.test_api(host_t, host_d, token_t, token_d, d)
        if result == 'PASS':
            sum_pass = sum_pass + 1
        else:
            sum_fail = sum_fail + 1
    print("本次共请求{0}个接口，接口响应一致的{1}个，接口响应不一致的{2}个".format(sum_pass + sum_fail, sum_pass, sum_fail))
    # APIDIFF.test_api(host_t, host_d, token_t, token_d, testData[32])
