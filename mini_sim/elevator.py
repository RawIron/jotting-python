def test_return_to_ground():
    at_floor = 4
    to_floor = 0
    incoming = []
    moves = run(at_floor, to_floor, incoming)
    assert moves == [4, 3, 2, 1, 0]

def test_stay():
    at_floor = 0
    to_floor = 0
    incoming = []
    moves = run(at_floor, to_floor, incoming)
    assert moves == [0]

def test_up_down_up_ground():
    at_floor = 2
    to_floor = 3
    incoming = [[2], [], [3]]
    moves = run(at_floor, to_floor, incoming)
    assert moves == [2, 3, 2, 3, 2, 1, 0]

def test_down_down_ground():
    at_floor = 0
    to_floor = -1
    incoming = [[], [-2]]
    moves = run(at_floor, to_floor, incoming)
    assert moves == [0, -1, -2, -1, 0]


def move(position, target):
    if position < target: return position + 1
    elif position > target: return position - 1
    else: return position


def arrived(position, target):
    return position == target


def serve(position, target, requests):
    if arrived(position, target):
        if not requests:
            return (move(position, 0), 0, [])
        else:
            return (move(position, requests[0]), requests[0], requests[1:])
    else:
        return (move(position, target), target, requests)


def run(at_floor, to_floor, incoming):
    moves = [at_floor]
    target = to_floor
    requests = []
    while not arrived(at_floor, target) or target != 0 or requests:
        if incoming:
            requests += incoming[0]
            incoming = incoming[1:]
        at_floor, target, requests = serve(at_floor, target, requests)
        moves.append(at_floor)
    return moves


if __name__ == "__main__":
    test_stay()
    test_return_to_ground()
    test_up_down_up_ground()
    test_down_down_ground()
