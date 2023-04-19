import yaml
from pathlib import Path


def read_yaml(yaml_path):
    try:
        with open(yaml_path, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    except IOError:
        print('config file not found')


def config():
    config = read_yaml(filepath)
    return config


projectPath = Path(__file__).parent.parent  # 获取当前项目的路径
filepath = str(projectPath) + '/config.yaml'

browser = config()['browser']
url = config()['url']
username = config()['username']
password = config()['password']
