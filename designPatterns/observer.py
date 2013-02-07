#!/usr/bin/python


class Observer(object):
    def update(self, event):
        raise NotImplementedError

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
        if self.isEarned():
            print "go nuts"
    def isEarned(self):
        if self.counter > 10:
            return True
        else:
            return False

class Gun(Observable):
    def __init__(self):
        super(Gun, self).__init__()
        self.munition = 3

    def loaded(self):
        return (munition > 0)

    def fire(self):
        if not self.loaded:
            return
        self.munition -= 1
        self.notify(9)


if __name__ == '__main__':
    watch = Achievement()
    g = Gun()
    g.subscribe(watch)
    g.fire()
    g.fire()
    g.unsubscribe(watch)
    g.fire()

