
from sim import Simulator, Job, Event


def test_post(sim):
    events = []

    job = Job()
    job.load(8)
    event = Event(1,job)
    events.append(event)

    job = Job()
    job.load(1)
    event = Event(7,job)
    events.append(event)

    job = Job()
    job.load(12)
    event = Event(3,job)
    events.append(event)

    for event in events:
        sim.post(event)



sim = Simulator()
test_post(sim)
sim.simulate()

