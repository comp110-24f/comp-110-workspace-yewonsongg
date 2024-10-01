"""concatenation"""

__author__ = "730771673"


def concat(word1: str, word2: str) -> str:
    """concatenations or combines 2 words into 1"""
    return word1 + word2


if __name__ == "__main__":
    """makes the functions within the function global (can import to other files)"""
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
    """these don't get imported because it's outside of the if name function"""
