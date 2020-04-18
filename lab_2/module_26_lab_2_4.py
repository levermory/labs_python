# flatten_it


def flatten_it(iter_object):
    """Flattens any iterable argument

    """
    for element in iter_object:
        try:
            if element.__len__() != 1:
                flatten_it(element)
            else:
                print(element, end=' ')
        except AttributeError:
            print(element, end=' ')


if __name__ == "__main__":
    test = [1, ['b', [3, 'c', [5, 'c']]]]
    test[0] = test
    flatten_it(test)
