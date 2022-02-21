from werkzeug.exceptions import BadRequest


def validate_body(data: dict, **kwargs) -> dict:
    missing_keys = [key for key in kwargs.keys() if key not in data.keys()]

    if missing_keys:
        raise BadRequest(description={"error": f"missing keys: {missing_keys}"})

    invalid_types = {
        "error": f"Invalid type, `{key}` type should be {value} but was {type(data[key])}"
        for key, value in kwargs.items()
        if type(data[key]) != value
    }

    if invalid_types:
        raise BadRequest(invalid_types)

    return {key: data[key].lower() for key in kwargs.keys()}
