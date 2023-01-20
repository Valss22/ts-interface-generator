from .type_conversion import python_type_to_ts_type


def dict_to_typescript(data: dict, name: str):
    interface_str = "interface {name} {{\n".format(name=name)
    for field in data:
        interface_str += f"  {field}: {python_type_to_ts_type(data[field])}\n"
    interface_str += "}\n"
    return interface_str


data = {"name": str, "age": int, "isActive": bool, "scores": list}
print(dict_to_typescript(data, "Person"))
