import guess_game, currency_roulette_game, memory_game, score, main_score

def welcome():
    username = input('Hello explorer! What is your name?: ')
    print(f'Lord {username}! welcome to the World of Games: The Epic Journey.')

def start_play():
    while True:
        game_choice = input(
              'Choose a game to play: \n'
              '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n'
              '2. Guess Game - guess a number and see if you chose like the computer.\n'
              '3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n'
              '4. Exit\n')

        if str.isdigit(game_choice) and 0 < int(game_choice) < 5:
            if int(game_choice) == 4:
                print("Goodbye!")
                break

            main_score.score_server()
            while True:
                difficulty = input('Now, choose your difficulty between 1-5: ')

                if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
                    difficulty = int(difficulty)
                    print(f'You selected difficulty {difficulty}. Let\'s begin!')
                    break
                else:
                    print('Choose a number between 1-5 only')

            if int(game_choice) == 1:
                result = memory_game.play(int(difficulty))
                if result:
                    print('WIN')
                    score.add_score(difficulty)
                else:
                    print('Try again')

            elif int(game_choice) == 2:
                result = guess_game.play(int(difficulty))
                if result:
                    print('WIN')
                    score.add_score(difficulty)
                else:
                    print('Try again')

            elif int(game_choice) == 3:
                if currency_roulette_game.play(int(difficulty)):
                    print('WIN')
                    score.add_score(difficulty)
                else:
                    print('Try again')
        else:
            print('Please choose one of the numbers above.')

if __name__ == "__main__":
    welcome()
    start_play()