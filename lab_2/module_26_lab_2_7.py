# leonardo num

import argparse


def leo(n):
    """functions which returns n-th Leonardo number"""
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return leo(n-1) + leo(n-2) + 1


def if_leo(number):
    i = 0
    while leo(i) <= number:
        if leo(i) == number:
            return True
        i += 1
    return False


def check():
    print("\nEnter 'stop' to stop.\n")
    while True:
        users_input = input("Enter your number:")
        if users_input == "stop":
            print("Have a nice day!")
            break
        else:
            try:
                number_to_check = int(users_input)
                print(if_leo(number_to_check))
            except ValueError:
                print("Wrong input")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', nargs='?', type=int)
    namespace = parser.parse_args()
    if namespace.number:
        print(if_leo(namespace.number))
    else:
        check()

