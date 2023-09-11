def create_dictionary(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        key_str = str(key) if hashable(key) else repr(key)
        argument_dict[key_str] = value
    return argument_dict

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

result_dict = create_dictionary(a=1, b="Привет", c=[1, 2, 3], d={"name": "Шалкар"})
print(result_dict)