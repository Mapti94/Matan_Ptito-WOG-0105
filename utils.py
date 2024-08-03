import os


# A string representing a file name.
SCORES_FILE_NAME = "score.txt"

# A number representing a bad return code for a function.
BAD_RETURN_CODE = 606

def clear_terminal():
    # Clear the terminal in a cross-platform way
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')
