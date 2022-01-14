from json import dump, load, JSONDecodeError


def read_json(filepath: str):
    try:
        with open(filepath, "r") as json_file:
            return load(json_file)
    except (FileNotFoundError, JSONDecodeError):
        return []


def write_json(filepath: str, payload: dict):
    json_list = read_json(filepath)
    json_list.append(payload)
    with open(filepath, "w") as json_file:
        dump(json_list, json_file, indent=2)

    return payload
