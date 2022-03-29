import json


def generate_diff(file_path1, file_path2):
    result = {}

    with open(file_path1) as file1, open(file_path2) as file2:
        dict1 = json.load(file1)
        dict2 = json.load(file2)

    keys = sorted(dict1.keys() | dict2.keys())
    for key in keys:
        result[key] = {}
        if key not in dict1:
            result[key]['type'] = 'added'
            result[key]['new_value'] = convert_bool_values(dict2[key])
        elif key not in dict2:
            result[key]['type'] = 'deleted'
            result[key]['old_value'] = convert_bool_values(dict1[key])
        elif dict1[key] == dict2[key]:
            result[key]['type'] = 'unchanged'
            result[key]['old_value'] = convert_bool_values(dict1[key])
        else:
            result[key]['type'] = 'changed'
            result[key]['old_value'] = convert_bool_values(dict1[key])
            result[key]['new_value'] = convert_bool_values(dict2[key])
    return convert_to_string(result)


def convert_to_string(user_dict):
    result = []
    for k, v in user_dict.items():
        if v['type'] == 'unchanged':
            line = '    {}: {}'.format(k, v['old_value'])
        if v['type'] == 'added':
            line = '  + {}: {}'.format(k, v['new_value'])
        if v['type'] == 'deleted':
            line = '  - {}: {}'.format(k, v['old_value'])
        if v['type'] == 'changed':
            line1 = '  - {}: {}'.format(k, v['old_value'])
            line2 = '  + {}: {}'.format(k, v['new_value'])
            line = '\n'.join([line1, line2])
        result.append(line)
    return '{\n' + '\n'.join(result) + '\n}'


def convert_bool_values(value):
    convert_dict = {True: 'true', False: 'false', None: 'null'}
    if value in convert_dict:
        return convert_dict[value]
    return value

print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))