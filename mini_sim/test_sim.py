
from sim import *


def test_event_queue_what_goes_in_comes_out():
    eq = EventQueueMixin()
    e_1 = Event(1,1)
    eq.post(e_1)
    eo_1 = eq.pull()
    assert (eo_1 == e_1)


def test_event_queue_smallest_of_two_comes_out_first():
    eq = EventQueueMixin()
    e_1 = Event(1,1)
    eq.post(e_1)
    e_3 = Event(3,3)
    eq.post(e_3)
    eo_1 = eq.pull()
    assert (eo_1 == e_1)


def test_event_queue_smallest_is_always_first():
    eq = EventQueueMixin()
    e_3 = Event(3,3)
    eq.post(e_3)

    e_1 = Event(1,1)
    eq.post(e_1)
    e_7 = Event(7,7)
    eq.post(e_7)
    eo_1 = eq.pull()
    assert (eo_1 == e_1)

    e_9 = Event(9,9)
    eq.post(e_9)
    e_5 = Event(5,5)
    eq.post(e_5)
    eo_3 = eq.pull()
    assert (eo_3 == e_3)

    eo_5 = eq.pull()
    assert (eo_5 == e_5)


def _run_simulate(sim, events):
    for event in events:
        sim.post(event)
    sim.simulate()



def test_delay_action():
    sim = Simulator()
    events = []

    action = DelayAction(sim, 8)
    load = [action]
    worker = Worker(load)
    event = Event(1,worker)
    events.append(event)

    action = DelayAction(sim, 3)
    load = [action]
    worker = Worker(load)
    event = Event(7,worker)
    events.append(event)

    action = DelayAction(sim, 2)
    load = [action]
    action = DelayAction(sim, 9)
    load.append(action)
    worker = Worker(load)
    event = Event(3,worker)
    events.append(event)

    _run_simulate(sim, events)


def test_put_action_increases_quantity_in_resource():
    sim = Simulator()
    events = []

    stash = Resource(sim)
    action = PutAction(sim, stash, 8)
    load = [action]
    worker = Worker(load)
    event = Event(1,worker)
    events.append(event)

    _run_simulate(sim, events)

    assert (stash.stock == 8)
    assert (not stash.put_queue)


def test_take_action_decreases_quantity_in_resource():
    sim = Simulator()
    events = []

    stash = Resource(sim)
    action = PutAction(sim, stash, 8)
    load = [action]
    action = TakeAction(sim, stash, 4)
    load.append(action)
    worker = Worker(load)
    event = Event(1,worker)
    events.append(event)

    _run_simulate(sim, events)

    assert (stash.stock == 4)
    assert (not stash.put_queue)
    assert (not stash.take_queue)

    
    
