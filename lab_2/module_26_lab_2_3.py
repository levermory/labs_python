import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', default='test.txt')
    return parser


def merge_sort(array):
    if len(array) > 1:
        mid = array.__len__()//2
        left_sub = array[:mid]
        right_sub = array[mid:]

        merge_sort(left_sub)
        merge_sort(right_sub)

        i = j = k = 0

        while i < left_sub.__len__() and j < right_sub.__len__():
            if left_sub[i] < right_sub[j]:
                array[k] = left_sub[i]
                i += 1
            else:
                array[k] = right_sub[j]
                j += 1
            k += 1

        while i < left_sub.__len__():
            array[k] = left_sub[i]
            i += 1
            k += 1

        while j < right_sub.__len__():
            array[k] = right_sub[j]
            j += 1
            k += 1


if __name__ == '__main__':
    cmdline_parser = create_parser()
    namespace = cmdline_parser.parse_args()

    with open('merged.txt', 'w') as write_file:
        with open(namespace.file, 'r') as read_file:
            for line in read_file:
                array = line.split()
                merge_sort(array)
                write_file.write(" ".join(array))
