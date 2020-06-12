# flatten_it

import argparse


def flatten_it(list):
    """Flattens any iterable argument.

    """
    result = []

    def flattener(iter_object):

        nonlocal result
        for element in iter_object:
            try:
                if type(element) == str:
                    result.append(element)
                elif element.__len__() != 1:
                    flattener(element)
                else:
                    result.append(element)
            except AttributeError:
                result.append(element)
            except RecursionError:
                raise ValueError

    flattener(list)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='*', type=eval, default=[1, ['b', [3, 'c', [5, 'cfhfhtf']]]])
    namespace = parser.parse_args()

    res = flatten_it(namespace.input)
    print(res)
