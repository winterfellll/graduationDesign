import os
import pytest
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    pytest.main(['TestCase/', '-s', '-q', '--clean-alluredir', '--alluredir=./allure-results'])
    os.system(r"allure generate -c -o ./TestReport")
