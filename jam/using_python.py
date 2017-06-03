'''
http://usingpython.com/python-programming-challenges/
'''


def _reverse_string(str):
    return str[::-1]


def print_banner(headline, marker='*', filler='.:: '):
    width = len(headline) + 2* len(filler)

    print(marker * width)
    print(filler + headline + filler[::-1])
    print(marker * width)


def mastermind():
    import random
    from six.moves import input, range

    precision = 4
    prompt = '> '

    def print_cracked(blacks, whites):
        print('*' * whites + '+' * blacks)


    def count_cracked(guess, code):
        blacks = 0
        whites = 0
        for ix, n in enumerate(guess):
            if int(n) == code[ix]:
                blacks += 1
            elif int(n) in code:
                whites += 1
        return blacks, whites


    def is_cracked(blacks, whites):
        return (blacks + whites == precision)


    code = [random.randint(0,9) for n in range(precision)]

    tries = 0
    blacks = 0
    whites = 0
    while not is_cracked(blacks, whites):
        tries += 1
        guess = input(str(tries) + prompt)
        blacks, whites = count_cracked(guess, code)
        print_cracked(blacks, whites)


