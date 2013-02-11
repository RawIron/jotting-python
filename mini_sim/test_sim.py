
from sim import Simulator, Worker, Event, DelayedAction, EventQueueMixin


def test_event_queue():
    eq = EventQueueMixin()
    e_3 = Event(3,3)
    eq.post(e_3)

    e_1 = Event(1,1)
    eq.post(e_1)
    eo_1 = eq.pull()
    assert (eo_1 == e_1)

    e_7 = Event(7,7)
    eq.post(e_7)
    e_9 = Event(9,9)
    eq.post(e_9)
    eo_3 = eq.pull()
    assert (eo_3 == e_3)

    eo_7 = eq.pull()
    print eo_7, e_7
    assert (eo_7 == e_7)


def test_sim():
    sim = Simulator()
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

    sim.simulate()

test_sim()
