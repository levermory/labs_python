# big files generator

from random import choice
from random import randint
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?', default='test')
    parser.add_argument('size', nargs='?', default=1, type=int)
    parser.add_argument('-k', '--k', nargs=2, default=(10, 100), type=int)
    parser.add_argument('-l', '--l', nargs=2, default=(3, 10), type=int)
    return parser


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


def generate_file(file_name, file_size, K=(10, 100), L=(3, 10)):
    """Generates file 'file_name.txt' of 'size'MBs
    with K words per line, each word is of L letters.

    """
    file_size *= 1024 ** 2
    progress = 0
    with open("{}.txt".format(file_name), 'w') as file:
        while True:
            text_line = random_line(L, K)
            if progress+len(text_line) >= file_size:
                break
            file.write(text_line)
            progress += len(text_line)
            print('\r','%', round(progress/file_size, 3) * 100,  end='')
        while progress < file_size:
            file.write(' ')
            progress += 1


if __name__ == "__main__":
    cmdline_parser = create_parser()
    namespace = cmdline_parser.parse_args()
    generate_file(namespace.name, namespace.size, namespace.k, namespace.l)
