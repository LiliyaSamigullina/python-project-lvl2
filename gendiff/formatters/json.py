import json


def format_json(user_dict: dict) -> str:
    return json.dumps(user_dict, sort_keys=True)
