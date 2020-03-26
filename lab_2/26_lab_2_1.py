# sqrt decomposition

from math import sqrt


def sqrt_decomposition(array):
    n = int(sqrt(len(array)))
    blocks = []
    block = 0
    for i in range(len(array)):
        block += array[i]
        if (i + 1) % n == 0:
            blocks.append(block)
            block = 0
        elif i == len(array) - 1:
            blocks.append(block)

    def request(some_var):
        some_var = some_var.split()
        if len(some_var) != 2:
            print("Error: wrong request.")
        else:
            i = left = int(some_var[0])
            right = int(some_var[1])
            if left < 0 or right > len(array):
                print("Error: wrong request.")
            else:
                temp_sum = 0
                if left == right:
                    return array[left]
                while i <= right:
                    if i % n == 0 and i + n - 1 <= right:
                        temp_sum += blocks[int(i / n)]
                        i += n
                    else:
                        temp_sum += array[i]
                        i += 1
                return temp_sum
    return request


def file_operation():
    with open('requests.txt') as file:
        array = list(file.readline().split())
        for i in range(len(array)):
            array[i] = int(array[i])
        file_array = sqrt_decomposition(array)
        for line in file:
            print(file_array(line))


def input_operations():
    users_input = input("Enter array: ")
    while True:
        if users_input == "end":
            break
        temp_array = users_input.split()
        for i in range(len(temp_array)):
            temp_array[i] = int(temp_array[i])
        input_array = sqrt_decomposition(temp_array)
        print(input_array(input("Enter your request: ")))


print("Welcome to sqrt-decompositor!\n\
To read the array and requests from\n\
\"requests.txt\" file please type \"file\"\n\
To input data manually type \"input\"\n\
Please, type your requests as \"int space int\",\n\
e.g. \"4 5\".\n\
Or you may enter \"stop\" if you want to cancel.")

while True:
    command = input("Enter your command: ")
    if command == "stop":
        break
    elif command == "file":
        file_operation()
    elif command == "input":
        input_operations()
    else:
        print("unknown command")
