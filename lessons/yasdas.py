def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    N: int = 1
    while N <= 6:
        print(f"=== Turn {N}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {N} turns!")
            return
        N += 1
    print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    guess_word: str = input(f"Enter a {secret_word_len} character word")
    while len(guess_word) != secret_word_len:
        guess_word = input(f"That wasn't {secret_word_len}! Try again: ")
    return guess_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    index = 0
    in_the_word = False
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            in_the_word = True
        index += 1
    return in_the_word


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    result: str = ""
    while index < len(guess):
        if len(guess) == len(secret):
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    return result


if __name__ == "__main__":
    main(secret="codes")
