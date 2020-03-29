# dvoika degree


def if_degree(number):
    """Bool function which checks if an argument is
    a accurate degree of 2.

    """

    number = list(bin(number))
    del number[:2]
    number = list(map(int, number))
    check = sum(number)
    if check == 1:
        return True
    else:
        return False


def check():
    print("Enter 'stop' to stop. \n")
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
    check()
