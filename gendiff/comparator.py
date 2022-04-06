def get_diff_dict(dict1, dict2):
    diff_dict = {}

    keys = dict1.keys() | dict2.keys()
    for key in keys:
        diff_dict[key] = {}
        if key not in dict1:
            diff_dict[key]['type'] = 'added'
            diff_dict[key]['value'] = dict2[key]
        elif key not in dict2:
            diff_dict[key]['type'] = 'deleted'
            diff_dict[key]['value'] = dict1[key]
        elif dict1[key] == dict2[key]:
            diff_dict[key]['type'] = 'unchanged'
            diff_dict[key]['value'] = dict1[key]
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff_dict[key] = {
                'type': 'nested',
                'value': get_diff_dict(dict1[key], dict2[key])
            }
        else:
            diff_dict[key]['type'] = 'changed'
            diff_dict[key]['old_value'] = dict1[key]
            diff_dict[key]['new_value'] = dict2[key]
    return diff_dict
