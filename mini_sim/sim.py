
from heapq import heappush, heappop


schedule = []
ticks = 5
events = [[1,8], [7,1], [3,12],]


class Job(object):
    def load(self, this):
        self.load = this
    def run(self):
        print self.load

def post():
    for event in events:
        run_at = event[0]
        what = event[1]
        job = Job()
        job.load(what)
        heappush(schedule, [run_at, job])

def tick():
    try:
        event = heappop(schedule)
        event[1].run()
    except IndexError:
        pass
    global ticks
    ticks -= 1

def stop():
    return (ticks < 0)

def simulate():
    while not stop():
        tick()

post()
simulate()
