import os

import pytest

if __name__ == '__main__':
    # pytest.main(['demo_testcase_request_test.py', '-s', '-q', '--clean-alluredir', '--alluredir=allure-results'])
    # os.system(r"allure generate -c -o Report")
    os.system('hrun demo_testcase_request.yml  --alluredir allure_results --clean-alluredir')
    os.system('allure generate --clean allure_results -o Report/')
