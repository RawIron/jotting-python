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
    blacks = 0
    whites = 0
    for ix, n in enumerate(guess):
        if int(n) == code[ix]:
            blacks += 1
            code[ix] = -1
    for ix, n in enumerate(guess):
        if code[ix] != -1 and int(n) in code:
            whites += 1
            code[code.index(int(n))] = -1
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


play(generate_code(), count_cracked, is_cracked, print_cracked)

