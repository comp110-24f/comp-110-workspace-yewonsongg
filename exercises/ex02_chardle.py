"""chardle assignment"""

__author__ = "730771673"


def input_word() -> str:
    # where user inputs a word with 5 letters
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        # word input must be 5 letters
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    # where user inputs a letter
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        # letter input must be 1 letter
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    x = 0  # x is the number of correcting letters
    if str(word)[0] == letter:
        print(letter + " found at index 0")
        x += 1  # if the letter is correct, number of characters increase by 1
    if str(word)[1] == letter:
        print(letter + " found at index 1")
        x += 1
    if str(word)[2] == letter:
        print(letter + " found at index 2")
        x += 1
    if str(word)[3] == letter:
        print(letter + " found at index 3")
        x += 1
    if str(word)[4] == letter:
        print(letter + " found at index 4")
        x += 1
    if x == 0:
        print("No instances of " + letter + " found in " + word)
        # in the case that no letter matches the word
    elif x == 1:
        # in the case that 1 letter matches the word
        print(str(x) + " instance of " + letter + " found in " + word)
    else:
        # in the case that 2 or more letters matches the word
        print(str(x) + " instances of " + letter + " found in " + word)


def main() -> None:
    # calling the function
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
