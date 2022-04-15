import json


def format_plain(user_dict: dict, parent: str = '') -> str:
    result = []

    for key, value in sorted(user_dict.items()):
        if value['type'] == 'changed':
            line = "Property '{}' was updated. From {} to {}".format(
                format_key(key, parent),
                format_value(value['old_value']),
                format_value(value['new_value'])
            )
            result.append(line)
        elif value['type'] == 'removed':
            line = "Property '{}' was removed".format(format_key(key, parent))
            result.append(line)
        elif value['type'] == 'added':
            line = "Property '{}' was added with value: {}".format(
                format_key(key, parent),
                format_value(value['value'])
            )
            result.append(line)
        elif value['type'] == 'nested':
            line = format_plain(value['value'], format_key(key, parent))
            result.append(line)
    return '\n'.join(result)


def format_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return "'{}'".format(value)
    return value


def format_key(key: str, parent: str) -> str:
    if parent:
        return '{}.{}'.format(parent, key)
    return str(key)
