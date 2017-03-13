'''
'''

import pprint


def dim_matrix(m):
    return len(m), len(m[0])


def init_matrix(rows, columns, pattern=[]):
    m = [[0 for i in range(rows)] for j in range(columns)]
    for x,y,z in pattern:
        m[x][y] = z
    return m


def map_matrix(m, func):
    rows, columns = dim_matrix(m)
    result = init_matrix(rows, columns)

    for x in range(rows):
        for y in range(columns):
            result[x][y] = func(m, x, y)

    return result


def flatten_matrix(m):
    return [value for vector in m for value in vector]


def sum_matrix(m):
    return sum(flatten_matrix(m))


def around(x, left, right):
    if x == left-1:
        return right
    elif x == right+1:
        return left
    else:
        return x


def extract_matrix(m, x, y, distance):
    rows, columns = dim_matrix(m)
    return [[m[around(x+j, 0, rows-1)][around(y+i, 0, columns-1)] for i in range(-distance,distance+1)] for j in range(-distance,distance+1)]



def evaluate(world, x, y):
    neighbors = extract_matrix(world, x, y, 1)
    value = sum_matrix(neighbors)

    if world[x][y] == 0 and value > 2:
        return 1
    elif world[x][y] == 1 and value > 3:
        return 1
    else:
        return 0


def run(m, n, data, rules):
    new_world = init_matrix(m, n, data)
    pprint.pprint(new_world)

    lifes = sum_matrix(new_world)
    while lifes > 0 and lifes < m*n:
        new_world = map_matrix(new_world, rules)
        lifes = sum_matrix(new_world)
        pprint.pprint(new_world)



DATA = [(0,1),
        (1,0), (1,1),
        (3,1),
        (4,2)]

INPUT = [(x,y,1) for x,y in DATA]

run(5, 5, INPUT, evaluate)

