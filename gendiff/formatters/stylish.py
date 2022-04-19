import json


def get_indent(_lvl: int) -> str:
    return '    ' * _lvl


def format_stylish(user_dict: dict, _lvl=0) -> str:
    result = []
    prefix = {'added': '  + ', 'removed': '  - ', 'unchanged': '    '}
    for key, value in sorted(user_dict.items()):
        if value['type'] == 'changed':
            line1 = '{}{}{}: {}'.format(
                get_indent(_lvl),
                prefix['removed'],
                key,
                format_value(value['old_value'], _lvl + 1)
            )
            line2 = '{}{}{}: {}'.format(
                get_indent(_lvl),
                prefix['added'],
                key,
                format_value(value['new_value'], _lvl + 1)
            )
            line = '\n'.join([line1, line2])
        elif value['type'] == 'nested':
            line1 = '{}{}: '.format(
                get_indent(_lvl + 1),
                key
            )
            line2 = format_stylish(value['value'], _lvl + 1)
            line = ''.join([line1, line2])
        else:
            line = '{}{}{}: {}'.format(
                get_indent(_lvl),
                prefix[value['type']],
                key,
                format_value(value['value'], _lvl + 1)
            )
        result.append(line)
    lines = '\n'.join(result)
    return f'{{\n{lines}\n{get_indent(_lvl)}}}'


def format_value(value, _lvl):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)

    if isinstance(value, dict):
        result = []
        for internal_key, internal_val in value.items():
            if isinstance(internal_val, dict):
                line = '{}{}: {}'.format(
                    get_indent(_lvl + 1),
                    internal_key,
                    format_value(internal_val, _lvl + 1)
                )
            else:
                line = '{}{}: {}'.format(
                    get_indent(_lvl + 1),
                    internal_key,
                    format_value(internal_val, _lvl)
                )
            result.append(line)
        lines = '\n'.join(result)
        return f'{{\n{lines}\n{get_indent(_lvl)}}}'
    return value
