#!/usr/bin/python


targets = [12, 3, 45, 76]


class NearestFirst(object):
    def pickFrom(self, targets):
        return min(targets)

class FarestFirst(object):
    def pickFrom(self, targets):
        return max(targets)


class Gun(object):
    def __init__(self, targets, targetSelection):
        self.targets = targets
        self.targetSelection = targetSelection

    def fire(self):
        target = self.targetSelection.pickFrom(targets)
        print target



if __name__ == '__main__':
    pickTarget = NearestFirst()
    g = Gun(targets, pickTarget)
    g.fire()

    del g
    pickTarget = FarestFirst()
    g = Gun(targets, pickTarget)
    g.fire()

