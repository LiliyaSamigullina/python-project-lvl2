import json
import yaml


def get_dict(file_path):
    with open(file_path) as file:
        if file_path[-5:] == '.json':
            data = json.load(file)
        if file_path[-5:] == '.yaml' or file_path[-4:] == '.yml':
            data = yaml.safe_load(file)
    return data
