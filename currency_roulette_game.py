import requests
import random


def get_money_interval(difficulty):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_owctAsUvDXTbKl8CS9QosQnHdO4LQ9w1NU0PUdRa"
    resp = requests.get(url)
    ils_currency = resp.json()['data']['ILS']
    random_dollar = random.randint(0, 100)
    highest_number = random_dollar * ils_currency + 10 - difficulty
    lowest_number = random_dollar * ils_currency - 10 + difficulty
    print(f'Guess how much ${random_dollar} is in ILS₪: ')
    return highest_number, lowest_number


def get_guess_from_user():
    while True:
        user_guess = input('Please provide a number: ')
        if str.isdigit(user_guess):
            return float(user_guess)
        else:
            print('Input error - provide a number')


def compare_results(highest_number, lowest_number, user_guess):
    if highest_number > user_guess > lowest_number:
        return True
    else:
        return False


def play(difficulty):
    highest, lowest = get_money_interval(difficulty)
    user_guess = get_guess_from_user()
    return compare_results(highest, lowest, user_guess)

