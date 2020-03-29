# big files generator

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


def generate_file(file_name='test', size=1, K=(10, 100), L=(3, 10)):
    """Generates file 'file_name.txt' of 'size'MBs
    with K words per line, each word is of L letters.

    """
    size *= 1000 ** 2
    progress = 0
    with open("{}.txt".format(file_name), 'w') as file:
        while progress <= size:
            text_line = random_line(L, K)
            file.write(text_line)
            progress += len(text_line)
            print('\r', round(progress/size, 2) * 100, '%', end='')
        print('\n', abs(progress - size))
        # a bit of cheating, last line probably
        # won't satisfy L&K requirement
        file.truncate(size)


#%%
generate_file()

#%%
if __name__ == "__main__":
    file_name = input("enter file's name: ")
    size = int(input("enter size of your file(in MBs: "))
    K = input("Enter K(enter 'default' to use default value):")
    L = input("Enter L(enter 'default' to use default value):")

