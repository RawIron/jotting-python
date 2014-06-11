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

