import time

import requests
import pytest
from xToolkit import xfile
import jsonpath, json

base_url = 'https://hjems-api.aihoge.com'

result = xfile.read('./data.xls').excel_to_dict('sheet1')


class Test():
    @pytest.mark.parametrize('case', result)
    def test(self, case):
        # result = requests.request(method=case['请求方式'],
        #                           url=base_url + case['url'],
        #                           headers=eval(case['headers']),
        #                           params=eval(case['params参数']),
        #                           data=eval(case['data参数']))
        # a = result.json()
        # token = jsonpath.jsonpath(a, case['参数提取'])[0]

        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJodHRwOi8vaGplbXMtYXBpLmFpaG9nZS5jb20vYmFja2VuZC9zeXN0ZW0vYXV0aC9zaWduL2luIiwiaWF0IjoxNjc2NjI2MzExLCJleHAiOjE2NzY2Mjk5MTEsIm5iZiI6MTY3NjYyNjMxMSwianRpIjoiVUtkUHQzbksxT0NCZE1QNSIsInN1YiI6IjQ0OTU3MzgxMjAyMzUyNTM3NiIsInBydiI6IjUxMjJmZTA3ZTg1YmY1ZWExMTA2MTAzN2QzMGQxOGMyMjU3NWZlYWEifQ.PQTqKapww9xag6P757ZDfGbneXAd82Q07sg3eLJGF0zZOyskvLQS8js4B1OagmvKKw0eRc3JBVFFlbK3wtag6g'
        val = {}
        val['token'] = token
        print(eval(case['headers']))
