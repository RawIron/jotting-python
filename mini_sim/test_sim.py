from sim import *


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
    load = []

    stash = Resource(sim)
    action = PutAction(sim, stash, 8)
    load.append(action)
    worker = Worker(load)
    event = Event(1,worker)
    events.append(event)

    _run_simulate(sim, events)

    assert (stash.stock == 8)
    assert (not stash.put_queue)


def test_take_action_decreases_quantity_in_resource():
    sim = Simulator()
    events = []
    load = []

    stash = Resource(sim)
    action = PutAction(sim, stash, 8)
    load.append(action)
    action = TakeAction(sim, stash, 4)
    load.append(action)
    worker = Worker(load)
    event = Event(1,worker)
    events.append(event)

    _run_simulate(sim, events)

    assert (stash.stock == 4)
    assert (not stash.put_queue)
    assert (not stash.take_queue)


def test_take_action_on_empty_resource_keeps_request():
    sim = Simulator()
    events = []
    load = []

    stash = Resource(sim)
    action = TakeAction(sim, stash, 4)
    load.append(action)
    worker = Worker(load)
    event = Event(1,worker)
    events.append(event)

    _run_simulate(sim, events)

    assert (stash.stock == 0)
    assert (len(stash.take_queue) == 1)
    
