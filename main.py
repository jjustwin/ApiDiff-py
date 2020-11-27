__author__ = 'tjw'

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest, requests, ddt
from config import setting
from lib.readexcel import ReadExcel
from lib.sendrequests import SendRequests

# from lib.writeexcel import WriteExcel

testData = ReadExcel(setting.SOURCE_FILE, "Sheet1").read_data()


@ddt.ddt
class apiDiff(unittest.TestCase):
    """API比较脚本"""

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self, data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[2])
        print("******* 正在执行用例 ->{0} *********".format(data['ID']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'], data['host1']))
        print("请求参数: {0}".format(data['params']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))
        # 发送请求
        re1,re2 = SendRequests().sendRequests(self.s, data)

        if re1.json() == re2.json():
            print("接口返回一致======================")
        if re1.json() != re2.json():
            print("请注意, %s 接口在两套环境中不一致", data['API'])
            print(data['host1'], "页面返回信息：%s" % re1.content.decode("utf-8"))
            print(data['host2'], "页面返回信息：%s" % re2.content.decode("utf-8"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
