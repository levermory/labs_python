# object to JSON


def parse_list(data):
    if type(data) == list or type(data) == tuple:
        result = '['
        for i in data:
            result += to_json(i) + ", "
        result += ']'
        return result


def parse_dict(data):
    if type(data) == dict:
        result = "{"
        for key, file in data.items():
            if type(key) not in (str, int):
                raise ValueError
            result += '  "{}": {}, '.format(key, to_json(file))
        result += "}"
        return result


def to_json(object):
    try:
         selector = {
            type(object) == str:'"{}"'.format(object) ,
            type(object) == int or float: "{}".format(object),
            type(object) == bool: "{}".format(object),
            type(object) == dict: parse_dict(object),
            type(object) == list: parse_list(object),
            type(object) == tuple: parse_list(object),
            object is None: "null",
        }[True]

         return selector

    except KeyError:
        raise ValueError("not JSONable type")

if __name__ == '__main__':
    default_data = {"somebody": 1, "told": ["me", "the world"], "is gonna": None, "roll ": {"me": 2}}

    with open("data.txt", "w") as file:
        file.write(to_json(default_data))
