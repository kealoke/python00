import math


def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    obj_and_type = f"{object} {type(object)}"

    if object is None:
        print(f"Nothing: {obj_and_type}")
    elif obj_type is float and math.isnan(object):
        print(f"Cheese: {obj_and_type}")
    elif obj_type is int and object == 0:
        print(f"Zero: {obj_and_type}")
    elif obj_type is str and object == "":
        print(f"Empty: {obj_and_type}")
    elif obj_type is bool and object is False:
        print(f"Fake: {obj_and_type}")
    else:
        print("Type not found")
        return -1

    return 0
