import argparse
import tempfile
import os


def merge_sort(array):
    if len(array) > 1:
        mid = array.__len__() // 2
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


def merge_sort_file(file):
    size = os.path.getsize(file.name)

    if size > 419430400:
        left_sub = tempfile.TemporaryFile(mode='w+t')
        right_sub = tempfile.TemporaryFile(mode='w+t')
        left_sub.writelines(file.readlines(size // 2))
        right_sub.writelines(file.readlines())

    else:

        temp_file = tempfile.TemporaryFile(mode='w+t')

        file_lines = file.readlines()
        merge_sort(file_lines)
        file.writelines(file_lines)
        temp_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', default='unmerged.txt')
    parser.add_argument('-o', '--output', default='merged.txt')
    namespace = parser.parse_args()
    unmerged_file = tempfile.TemporaryFile(mode='w+t')
    with open(namespace.file, 'r') as read_file:
        for line in read_file:
            array = line.split()
            merge_sort(array)
            unmerged_file.write(' '.join(array))
            unmerged_file.write('\n')
        with open(namespace.output, 'w') as write_file:
            merge_sort_file(unmerged_file)
            for line in unmerged_file:
                write_file.write(line)
