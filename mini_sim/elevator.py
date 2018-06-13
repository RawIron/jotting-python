def test_fifo_return_to_ground():
    at_floor = 4
    to_floor = 0
    incoming = []
    use_fifo = make_fifo()
    moves = run(at_floor, to_floor, make_serve(use_fifo), incoming)
    assert moves == [4, 3, 2, 1, 0]

def test_fifo_stay():
    at_floor = 0
    to_floor = 0
    incoming = []
    use_fifo = make_fifo()
    moves = run(at_floor, to_floor, make_serve(use_fifo), incoming)
    assert moves == [0]

def test_fifo_up_down_up_ground():
    at_floor = 2
    to_floor = 3
    incoming = [[2], [], [3]]
    use_fifo = make_fifo()
    moves = run(at_floor, to_floor, make_serve(use_fifo), incoming)
    assert moves == [2, 3, 2, 3, 2, 1, 0]

def test_fifo_down_down_ground():
    at_floor = 0
    to_floor = -1
    incoming = [[], [-2]]
    use_fifo = make_fifo()
    moves = run(at_floor, to_floor, make_serve(use_fifo), incoming)
    assert moves == [0, -1, -2, -1, 0]


def test_scan_down_down_ground():
    at_floor = 0
    to_floor = -1
    incoming = [[], [-2]]
    use_scan = make_scan()
    moves = run(at_floor, to_floor, make_serve(use_scan), incoming)
    assert moves == [0, -1, -2, -1, 0]

"""
    simulate one elevator
    an elevator is a device that
    moves between stops on a line
    only moves in two directions (previous stop, next stop)
    each stop is equally distant from the previous and the next stop

    0   1   2   3
    *---*---*---*   stops
     <--^-->        elevator
"""

UP = 1
DOWN = -1
IDLE = 0

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
    """
    direction uses previous position so it contains
    from which direction the elevator came from when it arrives at a floor
    """
    return (move(position, target), target, going(position, target), requests)

def arrived(position, target):
    return position == target

def going(position, target):
    if target - position < 0: return DOWN
    elif target - position > 0: return UP
    else: return IDLE

def no_more(requests):
    return not requests

def split_on_direction(position, requests):
    serve_down = []
    serve_up = []
    for r in sorted(requests):
        if r < position:
            serve_down.append(r)
        elif r > position:
            serve_up.append(r)
    return serve_down[::-1], serve_up

def make_fifo():
    def use_fifo(position, direction, requests):
        if no_more(requests):
            return (0, [])
        else:
            return (requests[0], requests[1:])
    return use_fifo

def make_scan():
    def use_scan(position, direction, requests):
        """
        the elevator continues to travel in its current direction (up or down) until empty
        stopping only to let individuals off
        or to pick up new individuals heading in the same direction
        """
        if no_more(requests):
            return (0, [])

        if direction == UP:
            serve_down, serve_up = split_on_direction(position, requests)
            if serve_up:
                return serve_up[0], serve_up[1:] + serve_down
            else:
                return serve_down[0], serve_down[1:]

        elif direction == DOWN:
            serve_down, serve_up = split_on_direction(position, requests)
            if serve_down:
                return serve_down[0], serve_down[1:] + serve_up
            else:
                return serve_up[0], serve_up[1:]

        else:
            raise ValueError
    return use_scan

def make_serve(pick_next_target):
    def serve(position, target, direction, requests):
        if arrived(position, target):
            target, requests = pick_next_target(position, direction, requests)
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
    direction = going(at_floor, to_floor)
    requests = []
    while not arrived(at_floor, target) or target != 0 or requests:
        requests, incoming = update(requests, incoming)
        at_floor, target, direction, requests = serve(at_floor, target, direction, requests)
        moves.append(at_floor)
    return moves


if __name__ == "__main__":
    test_fifo_stay()
    test_fifo_return_to_ground()
    test_fifo_up_down_up_ground()
    test_fifo_down_down_ground()
 
    test_scan_down_down_ground()
