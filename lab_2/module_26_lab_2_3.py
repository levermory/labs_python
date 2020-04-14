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
    file.seek(0)
    size = os.path.getsize(file.name)

    if size > 419430400:

        left_sub = tempfile.TemporaryFile(mode='w+t')
        right_sub = tempfile.TemporaryFile(mode='w+t')

        for line in file:
            if os.path.getsize(left_sub.name) <= size // 2:
                left_sub.write(line)
            else:
                right_sub.write(line)

        merge_sort_file(left_sub)
        merge_sort_file(right_sub)

    else:
        file_lines = file.readlines()
        merge_sort(file_lines)
        file.seek(0)
        file.writelines(file_lines)
        test_file.seek(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', default='unmerged.txt')
    parser.add_argument('-o', '--output', default='merged.txt')
    namespace = parser.parse_args()

    with open(namespace.file, 'r') as read_file:
        test_file = tempfile.TemporaryFile(mode='w+t')
        for line in read_file:
            array = line.split()
            merge_sort(array)
            test_file.write(' '.join(array))
            test_file.write('\n')
        test_file.seek(0)
        test_lines1 = test_file.readlines()
        merge_sort_file(test_file)
        test_lines2 = test_file.readlines()
        test_file.close()
        # with open(namespace.output, 'w+') as write_file:
        #     for line in read_file:
        #         array = line.split()
        #         merge_sort(array)
        #         write_file.write(' '.join(array))
        #         write_file.write('\n')
        #     merge_sort_file(write_file)
