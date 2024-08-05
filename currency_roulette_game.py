import random
from currency_converter import CurrencyConverter


def get_money_interval(difficulty):
    currency_converter = CurrencyConverter()
    usd_to_ils = currency_converter.convert(1, 'USD', 'ILS')
    random_amount_usd = random.randint(1, 100)
    print(f"Try to guess the value of {random_amount_usd}$ in ILS: ")
    upper_bound = usd_to_ils * random_amount_usd + (5 * (5 - difficulty))
    lower_bound = usd_to_ils * random_amount_usd - (5 * (5 - difficulty))
    return upper_bound, lower_bound


def get_guess_from_user():
    while True:
        user_input = input("Enter your guess: ")
        try:
            user_guess = float(user_input)
            return user_guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_results(upper_bound, lower_bound, user_guess):
    if lower_bound <= user_guess <= upper_bound:
        print("Congratulations, you guessed correctly!")
        return True
    else:
        print("That’s not correct. Better luck next time!")
        return False


def play(difficulty):
    bounds = get_money_interval(difficulty)
    upper = bounds[0]
    lower = bounds[1]
    return compare_results(upper, lower, get_guess_from_user())