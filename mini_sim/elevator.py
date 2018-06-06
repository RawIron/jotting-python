def test_fifo_return_to_ground():
    at_floor = 4
    to_floor = 0
    incoming = []
    moves = run(at_floor, to_floor, make_serve(use_fifo), incoming)
    assert moves == [4, 3, 2, 1, 0]

def test_fifo_stay():
    at_floor = 0
    to_floor = 0
    incoming = []
    moves = run(at_floor, to_floor, make_serve(use_fifo), incoming)
    assert moves == [0]

def test_fifo_up_down_up_ground():
    at_floor = 2
    to_floor = 3
    incoming = [[2], [], [3]]
    moves = run(at_floor, to_floor, make_serve(use_fifo), incoming)
    assert moves == [2, 3, 2, 3, 2, 1, 0]

def test_fifo_down_down_ground():
    at_floor = 0
    to_floor = -1
    incoming = [[], [-2]]
    moves = run(at_floor, to_floor, make_serve(use_fifo), incoming)
    assert moves == [0, -1, -2, -1, 0]

"""
    simulate one elevator
    an elevator a device that
    moves between stops on a line
    only moves in two directions (previous stop, next stop)
    each stop is equally distant from the previous and the next stop

    0   1   2   3
    *---*---*---*   stops
     <--^-->        elevator
"""

def go_up(position):
    return position + 1

def go_down(position):
    return position - 1

def stay_in(position):
    return position

def move(position, target):
    if position < target: return go_up(position)
    elif position > target: return go_down(position)
    else: return stay_in(position)

def step_to_target(position, target, requests):
    return (move(position, target), target, requests)

def arrived(position, target):
    return position == target


def no_more(requests):
    return not requests

def use_fifo(position, requests):
    if no_more(requests):
        return (0, [])
    else:
        return (requests[0], requests[1:])

def use_SCAN(position, direction, requests):
    """
    the elevator continues to travel in its current direction (up or down) until empty
    stopping only to let individuals off
    or to pick up new individuals heading in the same direction
    """
    pass

def make_serve(pick_next_target):
    def serve(position, target, requests):
        if arrived(position, target):
            target, requests = pick_next_target(position, requests)
        return step_to_target(position, target, requests)
    return serve


def update(requests, incoming):
    if incoming:
        requests += incoming[0]
        incoming = incoming[1:]
    return requests, incoming


def run(at_floor, to_floor, serve, incoming):
    moves = [at_floor]
    target = to_floor
    requests = []
    while not arrived(at_floor, target) or target != 0 or requests:
        requests, incoming = update(requests, incoming)
        at_floor, target, requests = serve(at_floor, target, requests)
        moves.append(at_floor)
    return moves


if __name__ == "__main__":
    test_fifo_stay()
    test_fifo_return_to_ground()
    test_fifo_up_down_up_ground()
    test_fifo_down_down_ground()
