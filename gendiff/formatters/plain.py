def format_plain(user_dict, parent=''):
    result = []

    for k, v in sorted(user_dict.items()):
        if v['type'] == 'changed':
            line = "Property '{}' was updated. From {} to {}".format(
                get_key(k, parent),
                get_value(v['old_value']),
                get_value(v['new_value'])
            )
            result.append(line)
        elif v['type'] == 'removed':
            line = "Property '{}' was removed".format(get_key(k, parent))
            result.append(line)
        elif v['type'] == 'added':
            line = "Property '{}' was added with value: {}".format(
                get_key(k, parent),
                get_value(v['value'])
            )
            result.append(line)
        elif v['type'] == 'nested':
            line = format_plain(v['value'], get_key(k, parent))
            result.append(line)
    return '\n'.join(result)


def get_value(v):
    convert_dict = {True: 'true', False: 'false', None: 'null'}
    if isinstance(v, bool) or v is None:
        return convert_dict[v]
    elif isinstance(v, dict):
        return '[complex value]'
    return "'{}'".format(v)


def get_key(k, parent):
    if parent:
        return '{}.{}'.format(parent, k)
    return str(k)
