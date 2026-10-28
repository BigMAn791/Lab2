print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
    print("display_main_menu")

def calc_average():
    print("calc_average")

def get_user_input():
    user_input = input("Enter a number:")
    user_list = user_input.split(",")
    numberlist = []
    for number in user_list:
        numberlist.append(float(number))
    return numberlist

def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")


display_main_menu()
numbers = get_user_input()
print("Your numbers:", numbers)