# flatten_it

import argparse


def flattener(iter_object):
    """Flattens any iterable argument

    """
    global result
    for element in iter_object:
        try:
            if element.__len__() != 1:
                flatten_it(element)
            else:
                result.append(element)
        except AttributeError:
            result.append(element)
        except RecursionError:
            raise ValueError
            
            
def flatten_if(list)
    result = []
    flattener(list)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='*', type=eval)
    namespace = parser.parse_args()

    # test = "[1, ['b', [3, 'c', [5, 'c']]]]"
    users_input = eval(namespace.input)
    print(flatten_it(users_input))
