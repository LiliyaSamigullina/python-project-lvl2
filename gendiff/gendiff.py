from gendiff.comparator import get_diff_dict
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parser import parse


def generate_diff(file_path1, file_path2, formatter='stylish'):
    dict1 = parse(file_path1)
    dict2 = parse(file_path2)
    result = get_diff_dict(dict1, dict2)
    if formatter == 'stylish':
        return format_stylish(result)
    if formatter == 'plain':
        return format_plain(result)
    if formatter == 'json':
        return format_json(result)
