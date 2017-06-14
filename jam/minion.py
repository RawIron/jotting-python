"""
minion game
https://www.hackerrank.com/challenges/the-minion-game
"""


def calculate_score(word):
    VOWELS = ['A', 'E', 'I', 'O', 'U']

    vowels = consonants = 0
    for ix, letter in enumerate(reversed(word)):
        if letter in VOWELS:
            vowels += ix + 1
        else:
            consonants += ix + 1

    return vowels, consonants


def play_minion(word):
    return calculate_score(word)
