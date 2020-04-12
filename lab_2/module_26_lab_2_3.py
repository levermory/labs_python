from random import choice
from random import randint


def random_letter():
    code_range = list(range(65, 122))
    del code_range[26:32]
    return chr(choice(code_range))


def random_word(L):
    length = randint(L[0], L[1])
    word = ""
    for i in range(length):
        word += random_letter()
    return word


def random_line(L, K):
    length = randint(K[0], K[1])
    line = ""
    for i in range(length):
        line = line + random_word(L) + ' '
    line += '\n'
    return line


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
    line = random_line((6, 10), (200, 200))
    array = line.split()

    merge_sort(array)
    print(array)
