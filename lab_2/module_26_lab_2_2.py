# big files generator
#%%
import sys
from random import choice

#%%
from random import choice
from random import randint


code_range = list(range(65, 122))
del code_range[26:32]

def random_letter():
    return chr(choice(code_range))


def random_word(L=(3, 10)):
    length = randint(L[0], L[1])
    word = ""
    for i in range(length):
        word += random_letter()
    return word


def random_line(K=(10, 100)):
    length = randint(K[0], K[1])
    line = ""
    for i in range(length):
        line = line + random_word() + ' '
    line += '\n'
    return line


#%%

def generate_file(size=1, K=(10, 100), L=(3, 10)):
    file_name = input("enter file's name: ")
    size = int(input("enter size of your file(in MBs: "))
    size *= 1000**2
    progress = 0
    with open("{}.txt".format(file_name), 'w') as file:
        while progress <= size:
            text_line = random_line()
            file.write(text_line)
            progress += len(text_line)
            print('\r', progress/size * 100, end='')
        file.truncate(size)


#%%
generate_file()

#%%
if __name__ == "__main__":
    code_range = list(range(65, 122))
    del code_range[26:32]
