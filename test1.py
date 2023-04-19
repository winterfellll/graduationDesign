# 根据字典的值value获得该值对应的key
def get_dict_key(dic, value):
    key = list(dic.keys())[list(dic.values()).index(value)]
    return key


def func(dict):
    for i in dict.values():
        if '$' in i:
            a = i.split('$')[1]
            dict[get_dict_key(dict, i)] = varDict[a]
    return dict


varDict = dict(token='Bearer adsuioqweqwedasd')  # 全局变量放在字典中
dic = {'token': '$token'}  # 实现 '$token' => dict1['token']
print(func(dic))
