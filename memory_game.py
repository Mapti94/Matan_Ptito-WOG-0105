import random
from time import sleep
import utils


def generate_sequence(difficulty):
    rand_list = [random.randint(1, 101) for _ in range(difficulty)]
    return rand_list


def get_list_from_user(difficulty, rand_list):
    print('Lets begin!')
    sleep(1.5)
    utils.clear_terminal()
    print('3')
    sleep(1.0)
    utils.clear_terminal()
    print('2')
    sleep(1.0)
    utils.clear_terminal()
    print('1')
    sleep(1.0)
    utils.clear_terminal()
    print(rand_list)
    sleep(0.7)
    utils.clear_terminal()

    user_input_list = []
    for i in range(difficulty):
        while True:
            try:
                user_input = int(input(f'Enter number {i + 1}: '))
                if 1 <= user_input <= 100:
                    user_input_list.append(user_input)
                    break
                else:
                    print('Input error. Enter a number between 1-100.')
            except ValueError:
                print('Input error. Make sure the input is a valid integer.')

    return user_input_list


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
