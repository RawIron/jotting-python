
from sim import Simulator, Worker, Event, DelayedAction


def test_post(sim):
    events = []

    action = DelayedAction(sim, 8)
    load = [action]
    worker = Worker(load)
    event = Event(1,worker)
    events.append(event)

    action = DelayedAction(sim, 3)
    load = [action]
    worker = Worker(load)
    event = Event(7,worker)
    events.append(event)

    action = DelayedAction(sim, 2)
    load = [action]
    action = DelayedAction(sim, 9)
    load.append(action)
    worker = Worker(load)
    event = Event(3,worker)
    events.append(event)

    for event in events:
        sim.post(event)



sim = Simulator()
test_post(sim)
sim.simulate()

