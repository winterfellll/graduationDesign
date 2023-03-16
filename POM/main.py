import os
import shutil
import time
from pathlib import Path

import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"allure generate -c -o Report")
    time.sleep(5)
    dir = projectPath = str(Path(__file__).parent.parent) + '/POM/allure-results'
    shutil.rmtree(dir)
    # pytest.main()
