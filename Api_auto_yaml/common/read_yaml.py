import yaml


def read(yaml_path):
    try:
        # 打开文件
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    except:
        return None
