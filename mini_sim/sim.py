
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
    def __init__(self, work_sequence):
        self.actions = work_sequence
        self.next = 0
    def work(self, current_tick):
        if len(self.actions) < self.next + 1:
            print "event at: %d" % current_tick
            return
        print "event at: %d" % current_tick
        action = self.actions[self.next]
        action.run(current_tick, self)
        self.next += 1

class EventQueueMixin(object):
    def __init__(self):
        self.event_queue = []
    def post(self, event):
        heappush(self.event_queue, (event.at_tick, event))
    def pull(self):
        next_entry = heappop(self.event_queue)
        event = next_entry[1]
        return event
    

class Simulator(EventQueueMixin):
    def __init__(self):
        super(Simulator, self).__init__()
        self.ticks = 50
        self.current_tick = 0

    def tick(self):
        event = self.pull()
        self.current_tick = event.at_tick
        event.worker.work(event.at_tick)

    def is_stopped(self):
        return not self.event_queue or (self.current_tick > self.ticks)

    def simulate(self):
        while not self.is_stopped():
            self.tick()

