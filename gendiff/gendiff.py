from gendiff.comparator import get_diff_dict
from gendiff.parser import get_dict
from gendiff.formatters.stylish import format_stylish


def generate_diff(file_path1, file_path2, formatter='stylish'):
    dict1 = get_dict(file_path1)
    dict2 = get_dict(file_path2)
    result = get_diff_dict(dict1, dict2)
    if formatter == 'stylish':
        return format_stylish(result)
