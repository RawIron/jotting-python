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
    '''
    make a copy of the code
    remove cracked digits from the copied code list
    '''
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


def count_cracked_separate_list(guess, code):
    '''
    use a separate list to store the cracked digits
    mark blacks as 1
    mark whites as 2
    '''

    def find_index(code, value, start):
        try:
            return code.index(int(value), start)
        except ValueError:
            return -1


    cracked = [0]*len(code)

    for ix, n in enumerate(guess):
        if int(n) == code[ix]:
            cracked[ix] = 1

    for ix, n in enumerate(guess):
        if cracked[ix] != 1:
            i = find_index(code, n, 0)
            while i >= 0 and cracked[i] > 0:
                i = find_index(code, n, i+1)
            if i >= 0 and cracked[i] == 0:
                cracked[i] = 2

    return len([n for n in cracked if n == 1]), len([n for n in cracked if n == 2])


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

