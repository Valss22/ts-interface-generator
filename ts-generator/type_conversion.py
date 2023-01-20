def python_type_to_ts_type(python_type) -> str:
    if python_type == str:
        return "string"
    elif python_type == int:
        return "number"
    elif python_type == float:
        return "number"
    elif python_type == bool:
        return "boolean"
    elif python_type == list:
        return "Array"
    elif python_type == dict:
        return "object"
    else:
        return python_type.__name__
