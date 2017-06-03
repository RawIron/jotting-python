'''
http://usingpython.com/python-programming-challenges/
'''


def _reverse_string(str):
    return str[::-1]


def _copy_list(x):
    return list(x)


def print_banner(headline, marker='*', filler='.:: '):
    width = len(headline) + 2* len(filler)

    print(marker * width)
    print(filler + headline + filler[::-1])
    print(marker * width)

