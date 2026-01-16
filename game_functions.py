import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if user_input == "h" and next_val > current_val:
        return True
    elif user_input == "l" and next_val < current_val:
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter in word:
        for c in range(len(word)):
            if letter == word[c]:
                board[c] = letter
        print(f"Well done! '{letter}' is in the word")
        return True

    else:
        print(f"Sorry, '{letter}' is not in the word")
        return False


