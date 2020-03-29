# sqrt decomposition

from math import sqrt


def sqrt_decomposition(array):
    """ Function returns sum on the [left, right]
    segment of the given array. Request must be
    a string of 2 integers and a space between them,
    e.g. "2 5".

    """
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
        i = left = some_var[0]
        right = some_var[1]
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
    """Enables user to read array and
    requests from file.

    """
    with open('requests.txt') as file:
        file_array = file.readline().split()
        try:
            file_array = list(map(int, file_array))
            decomposed_array = sqrt_decomposition(file_array)
            for request in file:
                request = list(map(int, request.split()))
                #            print(decomposed_array(request))
                try:
                    print(decomposed_array(request))
                except IndexError:
                    print("Wrong request", end='')
                    print(request)
        except ValueError:
            print("Wrong array")


#%% input
def input_operations():
    """Enables user to input array and requests manually.
    Array must be a string of numbers separated by spaces
    e.g.: "1 2 3 4 5…"

    """
    print("""Please, enter array like "1 2 3 4…".""")
    users_input = input("Enter array: ")
    try:
        users_input = list(map(int, users_input.split()))
        print(users_input)
        decomposed_array = sqrt_decomposition(users_input)
        print("To exit input mode type \"end\"")
        while True:
            users_input = input("Enter request: ")
            if users_input == "end":
                break
            else:
                users_input = list(map(int, users_input.split()))
                try:
                    print(decomposed_array(users_input))
                except IndexError:
                    print("Wrong request", end='')
                    print(users_input)
    except ValueError:
        print("Wrong array")


if __name__ == "__main__":
    print("""
Welcome to sqrt-decompositor!
To read the array and requests from
"requests.txt" file please type "file"
To input data manually type "input"
Please, type your requests as "int space int",
e.g. "4 5".
Or you may enter "stop" if you want to cancel. """)

    while True:
        command = input("Enter your command: ")
        if command == "stop":
            print("Have a nice day!")
            break
        elif command == "file":
            file_operation()
        elif command == "input":
            input_operations()
        else:
            print("unknown command")
