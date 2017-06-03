'''
http://usingpython.com/python-programming-challenges/

blacks = correct digit, correct position within code
whites = correct digit at wrong position
'''

import random
from six.moves import input, range

precision = 4

def print_cracked(blacks, whites):
    print('*' * whites + '+' * blacks)


def count_cracked(guess, code):
    _code = list(code)
    blacks = 0
    whites = 0
    for ix, n in enumerate(guess):
        if int(n) == _code[ix]:
            blacks += 1
            _code[ix] = -1
    for ix, n in enumerate(guess):
        if _code[ix] != -1 and int(n) in _code:
            whites += 1
            _code[_code.index(int(n))] = -2
    return blacks, whites


def is_cracked(blacks, whites):
    return (blacks + whites == precision)


def next_guess(tries):
    prompt = '> '
    return input(str(tries) + prompt)


def generate_code():
    return [random.randint(0,9) for n in range(precision)]


def play(code, count_cracked, is_cracked, print_cracked):
    tries = 0
    blacks = 0
    whites = 0
    while not is_cracked(blacks, whites):
        tries += 1
        blacks, whites = count_cracked(next_guess(tries), code)
        print_cracked(blacks, whites)


if __name__ == "__main__":
    play(generate_code(), count_cracked, is_cracked, print_cracked)

