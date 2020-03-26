# sqrt decomposition

from math import sqrt


def request(some_var):
    """Returns subsum of the array(sum
     of elements from 'left' to 'right').
     Request must
     be a string of 2 integers and a space
     between them, e.g.: "4 5".

     """
    some_var = some_var.split()
    i = left = int(some_var[0])
    right = int(some_var[1])
    temp_sum = 0
    if left == right:
        return array[left]
    while i <= right:
        if i % n == 0 and i + n - 1 <= right:
            temp_sum += Sums[int(i / n)]
            i += n
        else:
            temp_sum += array[i]
            i += 1
    return temp_sum


def file_operation():
    with open('requests.txt') as file:
        array = list(file.readline().split())
        for i in range(len(array)):
            array[i] = int(array[i])
        for line in file:
            print(request(line))


def read_array(input_string):
    temp_array = input_string.split()
    for i in range(len(temp_array)):
        temp_array[i] = int(temp_array[i])
    return temp_array


print("Welcome to sqrt-decompositor!\n\
Please, type your requests as \"int space int\",\n\
e.g. \"4 5\". Or you may enter \"stop\" if you want to cancel.\n\
To read the array and requests from \"requests.txt\" file please type \"file\" ")

while True:
    command = input("Enter your command: ")
    if command == "stop":
        break
    if command == "file":
        file_operation()
    if command == "input":
        array = read_array(input("Enter array: "))
    else:
        print("unknown command")

n = int(sqrt(len(array)))
Sums = []
Sum = 0
for i in range(len(array)):
    Sum += array[i]
    if (i + 1) % n == 0:
        Sums.append(sum)
        Sum = 0
    elif i == len(array) - 1:
        Sums.append(sum)



