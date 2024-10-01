"""practice with conditionals, local variables, and user input"""

__author__ = "730771673"


# user guesses a number
def guess_a_number() -> None:
    secret: int = 7  # the number the user is trying to guess
    x: int = int(input("Guess a number: "))  # where the user inputs their guess
    print("Your guess was " + str(x))

    if x == secret:  # if statement where user is correct
        print("You got it!")
    elif x < secret:  # else if statement where the user's guess is too low
        print("Your guess was too low! The secret number is " + str(secret))
    else:  # else statement where the user's guess is too high
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
