import random
from time import sleep


def generate_sequence(difficulty):
    rand_list = []
    for n in range(difficulty):
        rand_list.append(random.randint(1, 101))
    return rand_list


def get_list_from_user(difficulty, rand_list):
    print('Lets begin!'), sleep(1.5), print('\n' * 10)
    print('3'), sleep(1.0), print('\n' * 10)
    print('2'), sleep(1.0), print('\n' * 10)
    print('1'), sleep(1.0), print('\n' * 10)
    print(rand_list), sleep(0.7), print('\n' * 10)

    while True:
        user_input = input(f'Enter {difficulty} numbers from 1-100, separated by spaces: ')
        try:
            user_input_list = [int(item) for item in user_input.split()]
            if len(user_input_list) == difficulty and all(1 <= item <= 100 for item in user_input_list):
                return user_input_list
            else:
                print(f'Input error. Enter exactly {difficulty} numbers from 1-100.')
        except ValueError:
            print('Input error. Make sure all inputs are valid integers.')


def is_list_equal(rand_list, user_input_list):
    if rand_list == user_input_list:
        print(f"Debug: Comparing lists {rand_list} and {user_input_list}")
        return True
    else:
        return False


def play(difficulty):
    rand_list = generate_sequence(difficulty)
    user_input_list = get_list_from_user(difficulty, rand_list)
    return is_list_equal(rand_list, user_input_list)
