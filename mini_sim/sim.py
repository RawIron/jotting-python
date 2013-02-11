
from heapq import heappush, heappop


class Event(object):
    def __init__(self, at_tick, this_job):
        self.at_tick = at_tick
        self.job = this_job

class Job(object):
    def load(self, this):
        self.load = this
    def run(self):
        print self.load


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
            event.job.run()
        except IndexError:
            pass

    def stop(self):
        return (self.current_tick > self.ticks)

    def simulate(self):
        while not self.stop():
            self.tick()

