"""practicing my conditionals."""


def less_than_10(num: int) -> None:
    """tell us if num < 10."""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:  # check if this is true
        print("small number!")  # "then" block
    else:
        print("big number!")
    print("have a nice day!")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """return a message based on if alarm is going off"""
    if alarm is True:
        return "wake up! go to comp 110!"
    else:
        return "keep sleeping. u deserve it"


def check_first_letter(word: str, letter: str) -> str:
    """return ""match" if the first character of word is letter"""
    if word[0] is letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="hi", letter="h"))


def get_weather_report() -> str:
    weather: str = input("what is the weather?")
    if weather == "rainy" or weather == "cold":
        print("bring a jacket!")
    elif weather == "hot":
        print("keep cool out there!")
    else:
        print("i don't recognize this weather.")
        return weather


get_weather_report()
