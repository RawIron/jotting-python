
from heapq import heappush, heappop


class Event(object):
    def __init__(self, at_tick, this_worker):
        self.at_tick = at_tick
        self.worker = this_worker


class Action(object): pass

class DelayedAction(Action):
    def __init__(self, sim, delay):
        self.sim = sim
        self.delay = delay
    def run(self, started_at, worker):
        event = Event(started_at + self.delay, worker)
        self.sim.post(event)


class Worker(object):
    def __init__(self, work_on):
        self.load = work_on
        self.next = 0
    def work(self, current_tick):
        if len(self.load) < self.next + 1:
            return
        print current_tick
        action = self.load[self.next]
        action.run(current_tick, self)
        self.next += 1


class Simulator(object):
    def __init__(self):
        self.event_queue = []
        self.ticks = 5
        self.current_tick = 0

    def post(self, event):
        heappush(self.event_queue, [event.at_tick, event])

    def tick(self):
        next_entry = heappop(self.event_queue)
        event = next_entry[1]
        try:
            self.current_tick = event.at_tick
            event.worker.work(event.at_tick)
        except IndexError:
            pass

    def is_stopped(self):
        return (self.current_tick > self.ticks)

    def simulate(self):
        while not self.is_stopped():
            self.tick()

