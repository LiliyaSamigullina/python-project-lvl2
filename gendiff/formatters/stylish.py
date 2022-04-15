import json
TAB = '    '


def format_stylish(user_dict: dict, _lvl=0) -> str:
    indent = TAB * _lvl

    result = []
    prefix = {'added': '  + ', 'removed': '  - ', 'unchanged': '    '}
    for key, value in sorted(user_dict.items()):
        if value['type'] == 'changed':
            line1 = '{}{}{}: {}'.format(
                indent,
                prefix['removed'],
                key,
                format_value(value['old_value'], _lvl + 1)
            )
            line2 = '{}{}{}: {}'.format(
                indent,
                prefix['added'],
                key,
                format_value(value['new_value'], _lvl + 1)
            )
            line = '\n'.join([line1, line2])
        elif value['type'] == 'nested':
            line1 = '{}{}: '.format(
                (_lvl + 1) * TAB,
                key
            )
            line2 = format_stylish(value['value'], _lvl + 1)
            line = ''.join([line1, line2])
        else:
            line = '{}{}{}: {}'.format(
                indent,
                prefix[value['type']],
                key,
                format_value(value['value'], _lvl + 1)
            )
        result.append(line)
    return '{\n' + '\n'.join(result) + '\n' + indent + '}'


def format_value(value, _lvl):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)

    if isinstance(value, dict):
        result = []
        for internal_key, internal_val in value.items():
            if isinstance(internal_val, dict):
                line = '{}{}: {}'.format(
                    (_lvl + 1) * TAB,
                    internal_key,
                    format_value(internal_val, _lvl + 1)
                )
            else:
                line = '{}{}: {}'.format(
                    (_lvl + 1) * TAB,
                    internal_key,
                    format_value(internal_val, _lvl)
                )
            result.append(line)
        return '{\n' + '\n'.join(result) + '\n' + TAB * _lvl + '}'
    return value
