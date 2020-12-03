# -*- coding: utf-8 -*-
# @PROJECT : Aff_service
# @File    : replace_relevance.py


import re
import jsonpath


# from bin.unit import funcionTools

def replace(param, relvance:dict):
    """
    替换关联数据
    :param param: 请求参数
    :param relevance: 关联对象
    :return:
    """
    # 判断数据类型
    if isinstance(param, dict):
        # 遍历字典的键值对，赋值给key和value进行操作
        for key, value in param.items():
            # 如果value是个字典，就递归自己
            if isinstance(value, dict):
                param[key] = replace(value, relevance)
            # 如果value是个列表，就循环递归
            elif isinstance(value, list):
                for k, i in enumerate(value):
                    param[key][k] = replace(i, relevance)
            else:
                try:
                    # 正则匹配到所有的$(XXX)关键字
                    relevance_list = re.findall(r"\${(.*?)}", value)
                    # 遍历关键字列表
                    for n in relevance_list:
                        pattern = re.compile(r'\${' + n + r'}')
                        n = n.lower()
                        try:
                            # 从relvance中匹配关键字对应的依赖数据，用正则替换
                            param[key] = re.sub(pattern, str(relevance[n]), param[key], count=1)
                        except KeyError:
                            pass
                    # 上面替换完关键字后，判断是否存在**关键字
                    if value and '**' in str(value):
                        # 存在**关键字，说明这个字段内容需要被放大，用正则匹配出**[integer]
                        num = re.findall('\*\*(\d+)', value)[0]
                        # 数据可能为 a**20b，所以根据**num这个关键字分割出a,b，b也可能为空
                        v1, v2 = value.split(f'**{num}')
                        # 把a单独放大num的倍数，再加上b，就是放大之后的数据
                        param[key] = v1 * int(num) + v2
                    # # 正则匹配函数关键字，判断是否存在函数关键字:like---->$a() $a(1)
                    # funcs = re.findall("\$.+?\(.*?\)", value)
                    # if funcs:
                    #     # 遍历关键字列表
                    #     for func in funcs:
                    #         # 调用初始化函数参数方法去替换函数内容
                    #         param[key] = value.replace(func, str(funcionTools.initFuncParam(func[1:])))
                except TypeError:
                    pass
                try:
                    param[key] = param[key]
                except TypeError:
                    pass

    elif isinstance(param, list):
        for k, i in enumerate(param):
            param[k] = replace(i, relevance)
    else:
        try:
            relevance_list = re.findall(r"\${(.*?)}", param)
            for n in relevance_list:
                pattern = re.compile(r'\${' + n + r'}')
                n = n.lower()
                try:
                    if isinstance(relevance[n], list):
                        param = re.sub(pattern, relevance[n], param, count=1)
                    else:
                        param = re.sub(pattern, relevance[n], param)
                except KeyError:
                    pass
        except TypeError:
            pass

    return param


relvance = {}


def get_value(data, value):
    """
    获取json中的值
    :param data: json数据
    :param value: 值
    :return:
    """
    global relvance
    # 判断全局数据池中是否有jsonpath提值失败的数据，如果有，就把这个值删除
    if 'FALSE' in relvance.keys():
        del relvance['FALSE']
    # value ---->>>  k: $..v
    for k, v in value.items():
        # 初始化默认取第1个下标
        index = 0
        # 如果表达式格式为 #..data[?(@.k = 'v')].id[1],则判断v是否为]结尾
        if v.endswith(']'):
            # 按[分割v，['$..data','?(@.k = 'v')].id','1]']
            v = v.split('[')
            # 所以取的下标就是 1]
            index = v[-1]
            # 判断下标去掉]后是否为数字，如果是数字就把转为数字类型且下标改成这个数字
            if index[:-1].isdigit():
                index = int(index[:-1])  # index的结果为 1]   :-1的作用是干掉]
            # 如果表达式格式为$..data.id[2]时，不需要拼接，直接取分割后的第一个值就行，
            # 如果是上面的表达式，则需要把前面的字段拼起来$..data[?(@.k = 'v')].id
            if v.count('[') > 1:
                v = '['.join(v[:-1])
            else:
                v = v[0]
        # 使用jsonpath提值，成功返回一个值列表，不成功返回False
        result = jsonpath.jsonpath(data, v)
        # 判断提取是否成功，成功就往全局数据池中添加下标对应的值
        if result:
            relvance[k.lower()] = result[index]
        else:
            relvance['FALSE'] = result
    # 返回全局变量池
    return relvance
