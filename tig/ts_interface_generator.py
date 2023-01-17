def python_type_to_ts_type(python_type):
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


def dict_to_typescript(data: dict, name: str):
    interface_str = "interface {name} {{\n".format(name=name)
    for field in data:
        interface_str += f"  {field}: {python_type_to_ts_type(data[field])}\n"
    interface_str += "}\n"
    return interface_str


data = {"name": str, "age": int, "isActive": bool, "scores": list}
print(dict_to_typescript(data, "Person"))
