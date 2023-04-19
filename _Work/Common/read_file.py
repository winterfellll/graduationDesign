import yaml


def read_yaml(yaml_path):
    try:
        with open(yaml_path, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    except IOError:
        print('config file not found')


def config():
    config = read_yaml("../config.yaml")
    return config


browser = config()['browser']
url = config()['url']
username = config()['username']
password = config()['password']
