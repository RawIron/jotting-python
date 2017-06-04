'''
http://usingpython.com/python-programming-challenges/
'''


def reverse_string(str):
    return str[::-1]


def copy_list(x):
    return list(x)


def count_value(x, value):
    return x.count(value)


def count_value_comprehension(x, value):
    return len([n for n in x if n == value])


def count_value_functional(x, value):
    return len(filter(lambda y: y == value, x))


def count_value_iteration(x, value):
    count = 0
    for n in x:
        if n == value:
            count += 1
    return count


def print_banner(headline, marker='*', filler='.:: '):
    width = len(headline) + 2* len(filler)

    print(marker * width)
    print(filler + headline + filler[::-1])
    print(marker * width)

