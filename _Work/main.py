import os
import pytest

if __name__ == '__main__':
    pytest.main(['TestCase/', '-s', '-q', '--clean-alluredir', '--alluredir=./allure-results'])
    os.system(r"allure generate -c -o ./TestReport")
