TAB = '    '


def format_value(value, _lvl):
    convert_dict = {True: 'true', False: 'false', None: 'null'}
    if isinstance(value, bool) or value is None:
        return convert_dict[value]

    if isinstance(value, dict):
        result = []
        for k, v in value.items():
            if isinstance(v, dict):
                line = '{}{}: {}'.format(
                    (_lvl + 1) * TAB,
                    k,
                    format_value(v, _lvl + 1)
                )
            else:
                line = '{}{}: {}'.format(
                    (_lvl + 1) * TAB,
                    k,
                    format_value(v, _lvl)
                )
            result.append(line)
        return '{\n' + '\n'.join(result) + '\n' + TAB * _lvl + '}'
    return value


def format_stylish(user_dict, _lvl=0):
    indent = TAB * _lvl

    result = []
    prefix = {'added': '  + ', 'deleted': '  - ', 'unchanged': '    '}
    for k, v in sorted(user_dict.items()):
        if v['type'] == 'changed':
            line1 = '{}{}{}: {}'.format(
                indent,
                prefix['deleted'],
                k,
                format_value(v['old_value'], _lvl + 1)
            )
            line2 = '{}{}{}: {}'.format(
                indent,
                prefix['added'],
                k,
                format_value(v['new_value'], _lvl + 1)
            )
            line = '\n'.join([line1, line2])
        elif v['type'] == 'nested':
            line1 = '{}{}: '.format(
                (_lvl + 1) * TAB,
                k
            )
            line2 = format_stylish(v['value'], _lvl + 1)
            line = ''.join([line1, line2])
        else:
            line = '{}{}{}: {}'.format(
                indent,
                prefix[v['type']],
                k,
                format_value(v['value'], _lvl + 1)
            )
        result.append(line)
    return '{\n' + '\n'.join(result) + '\n' + indent + '}'
