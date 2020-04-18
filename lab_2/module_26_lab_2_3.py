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

    if size > 1048576 * 400:
        left_sub_file = tempfile.TemporaryFile(mode='w+t')
        right_sub_file = tempfile.TemporaryFile(mode='w+t')

        for line in file:
            if os.path.getsize(left_sub_file.name) <= size // 2:
                left_sub_file.write(line)
            else:
                right_sub_file.write(line)

        merge_sort_file(left_sub_file)
        merge_sort_file(right_sub_file)

        file.seek(0)
        left_sub_file.seek(0)
        right_sub_file.seek(0)

        left_line = left_sub_file.readline()
        right_line = right_sub_file.readline()

        while left_line and right_line:
            if left_line < right_line:
                file.write(left_line)
                left_line = left_sub_file.readline()
            else:
                file.write(right_line)
                right_line = right_sub_file.readline()

        while left_line:
            file.write(left_line)
            left_line = left_sub_file.readline()

        while right_line:
            file.write(right_line)
            right_line = right_sub_file.readline()

        left_sub_file.close()
        right_sub_file.close()

    else:
        global progress
        file_lines = file.readlines()
        merge_sort(file_lines)
        file.seek(0)
        file.writelines(file_lines)
        progress += len(file_lines)
        print('\r', '%', 50 + progress/line_count * 50, end='')
        file.seek(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', default='input.txt', type=argparse.FileType('r'))
    parser.add_argument('-o', '--output', default='output.txt', type=argparse.FileType('w+'))
    namespace = parser.parse_args()

    read_file = namespace.file
    write_file = namespace.output

    line_count = 0
    progress = 0

    for line in read_file:
        array = line.split()
        merge_sort(array)
        write_file.write(' '.join(array))
        write_file.write('\n')
        line_count += 1
        print('\r', '%', os.path.getsize(write_file.name)/os.path.getsize(read_file.name) * 50, end='')
    merge_sort_file(write_file)
