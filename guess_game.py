import random


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    # print(f'this is the secret number{secret_number}')
    return secret_number


def get_guess_from_user(difficulty):
    user_guess = input(f'provide a number between 0 to {difficulty}: ')
    return int(user_guess)


def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False


def play(difficulty):
    print('Welcome to the guess game\n')
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)

