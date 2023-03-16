import time

import pytest
import requests
import jsonpath, json
from common.read_yaml import read

base_url = 'https://hjems-api.aihoge.com'
path = './data/data.yml'


class Test():

    @pytest.mark.parametrize('case', read(path))
    def test(self, case):
        print(case['data'])
        # result = requests.request(method=case['method'],
        #                           url=base_url + case['url'],
        #                           headers=case['headers'],
        #                           params=case['params'],
        #                           data=case['data'])
        # json = result.json()
        #
        # print(json)
        # assert 'access_token' in json, '断言成功'

        # message = jsonpath.jsonpath(json, '$.error_message')[0]
        # if jsonpath.jsonpath(json, '$..access_token') != False:
        #     global token
        #     token = jsonpath.jsonpath(json, '$..access_token')[0]
