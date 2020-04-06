# dvoika degree

import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', nargs='?', type=int)
    return parser


def if_degree(number):
    """Bool function which checks if an argument is
    a accurate degree of 2.

    """

    number = list(bin(number))
    del number[:2]
    number = map(int, number)
    if sum(number) == 1:
        return True
    else:
        return False


def check():
    print("\nEnter 'stop' to stop. \n")
    while True:
        users_input = input("Enter your number:")
        if users_input == "stop":
            print("Have a nice day!")
            break
        else:
            try:
                number_to_check = int(users_input)
                print(if_degree(number_to_check))
            except ValueError:
                print("Wrong input")


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.number:
        print(if_degree(namespace.number))
    else:
        check()
