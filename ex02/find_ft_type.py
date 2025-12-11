def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "is in the kitchen"
    }

    if obj_type in type_names:
        type_name = type_names[obj_type]
        if obj_type is str:
            print(f"{object} {type_name} : {obj_type}")
        else:
            print(f"{type_name} : {obj_type}")
    else:
        print("Type not found")

    return 42
