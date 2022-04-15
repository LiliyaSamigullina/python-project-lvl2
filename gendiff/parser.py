import json
import yaml
import os


def get_format(file_path):
    return os.path.splitext(file_path)[-1][1:]


def parse(file_path):
    format_name = get_format(file_path)
    if format_name == 'json':
        with open(file_path) as file:
            return json.load(file)
    if format_name in {'yaml', 'yml'}:
        with open(file_path) as file:
            return yaml.safe_load(file)
    else:
        raise ValueError(f'Unknown format: {format_name}')
