# dvoika degree

#%%
def if_degree(number):
    number = list(bin(number))
    del number[:2]
    number = list(map(int, number))
    check = sum(number)
    if check == 1:
        return True
    else:
        return False


#%%
if __name__ == '__main__':
    print("Enter 'stop' to stop. \n")
    while True:
        users_input = input("Enter number:")
        if users_input == "stop":
            print("Have a nice day!")
            break
        else:
            try:
                number = int(users_input)
                print(if_degree(number))
            except ValueError:
                print("Wrong input")


