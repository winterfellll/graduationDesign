# 根据字典的值value获得该值对应的key
def get_dict_key(dic, value):
    key = list(dic.keys())[list(dic.values()).index(value)]
    return key


def func(dict):
    for i in dict.values():
        if '$' in i:
            a = i.split('$')[1]
            dict[get_dict_key(dict, i)] = eval('var' + a)
    return dict


vartoken = 'bearer adsuioqweqwedasd'

dic = {'token': '$token'}
print(func(dic))
