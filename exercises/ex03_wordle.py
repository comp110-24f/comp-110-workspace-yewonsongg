"""wordle assignment"""

__author__ = "730771673"


def main(secret: str) -> None:
    """entrypoint of program and main game loop"""
    N: int = 1
    # the number of turns to guess word; starts at 1
    while N <= 6:
        # N can't be more than 6 because there's only 6 tries
        print(f"=== Turn {N}/6 ===")
        # prints how many turns left
        guess = input_guess(len(secret))
        # enters the input_guess function to make sure length of guess is correct
        print(emojified(guess, secret))
        # matches letter by emoji
        if guess == secret:
            print(f"You won in {N}/6 turns!")
            # prints how many guesses made before win
            return
        N += 1
    print("X/6 - Sorry, try again tomorrow!")
    # prints if word isn't guessed


def input_guess(secret_word_len: int) -> str:
    # where user inputs a 5 letter word
    guess_word: str = input(f"Enter a {secret_word_len} character word: ")
    # f function connects strings together without using +; {} must be used for variable
    while len(guess_word) != secret_word_len:
        # word is 5 characters
        guess_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # guessed word is less or more than 5 characters
    return guess_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """function determines whether input word is correct or not"""
    assert len(char_guess) == 1
    index: int = 0
    in_the_word: bool = False
    # starts off False; enters loop if character guessed is in secret word
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            in_the_word = True
            # correct character is guessed; bool turns true
        index += 1
        # if false, it increases by 1 until true
    return in_the_word


def emojified(guess: str, secret: str) -> str:
    """function indicates whether word is guessed with emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    # unknown or doesn't exist in secret word
    GREEN_BOX: str = "\U0001F7E9"
    # is in the correct order of secret word
    YELLOW_BOX: str = "\U0001F7E8"
    # the character exists but not in the correct spot
    index: int = 0
    result: str = ""
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
            # correct letter is guessed in the correct spot; result is green box emoji
        elif contains_char(secret, guess[index]):
            # correct letter is guessed but incorrect spot; result is yellow box emoji
            result += YELLOW_BOX
        else:
            # incorrect letter; result is a white box emoji
            result += WHITE_BOX
        index += 1
    return result


if __name__ == "__main__":
    # the secret word is "codes"
    main(secret="codes")
