#!/usr/bin/python


class Observer(object):
    def update(self, event):
        pass

class Observable(object):
    def __init__(self):
        self.subscribers = []
    def subscribe(self, o):
        self.subscribers.append(o)
    def unsubscribe(self, o):
        self.subscribers.remove(o)
    def notify(self, event):
        for subscriber in self.subscribers:
            subscriber.update(event)


class Achievement(Observer):
    def __init__(self):
        self.counter = 0
    def update(self, event):
        self.counter += event
        self.check()
    def check(self):
        if self.counter > 10:
            print "got a prize"
        else:
            print "keep working"

class Gun(Observable):
    def fire(self):
        print "fired"
        self.notify(9)


if __name__ == '__main__':
    watch = Achievement()
    g = Gun()
    g.subscribe(watch)
    g.fire()
    g.fire()
    g.unsubscribe(watch)
    g.fire()

