#!/usr/bin/python

#
# state pattern does not work well here
#

class GunNullState(object):
    def fire(self, gun):
        pass
    def hit(self, gun):
        pass
    def upgrade(self, gun):
        pass
    def repair(self, gun):
        pass
    def enable(self, gun):
        gun.state = gun.states['ready']

class GunReadyState(object):
    def fire(self, gun):
        gun.bullets -= 1
    def hit(self, gun):
        gun.health -= 12
    def upgrade(self, gun):
        gun.state = gun.states['upgrade']
    def repair(self, gun):
        pass
    def enable(self, gun):
        pass

class GunUpgradeState(object):
    def fire(self, gun):
        pass
    def hit(self, gun):
        pass
    def upgrade(self, gun):
        pass
    def repair(self, gun):
        pass
    def enable(self, gun):
        gun.state = gun.states['ready']

class GunBrokenState(object):
    def fire(self, gun):
        pass
    def hit(self, gun):
        pass
    def upgrade(self, gun):
        pass
    def repair(self, gun):
        gun.state = gun.states['ready']
    def enable(self, gun):
        pass



class Gun(object):
    def __init__(self, initState, states):
        self.states = states
        self.state = initState
        self.health = 100
        self.bullets = 10

    def fire(self):
        self.state.fire(self)
    def hit(self):
        self.state.hit(self)
    def upgrade(self):
        self.state.upgrade(self)
    def repair(self):
        self.state.repair(self)
    def enable(self):
        self.state.enable(self)

    def dump(self):
        print self.health, self.bullets, self.state.__class__



if __name__ == '__main__':
    states = {}
    states['null'] = GunNullState()
    states['ready'] = GunReadyState()
    states['upgrade'] = GunUpgradeState()
    states['broken'] = GunBrokenState()

    gun = Gun(states['null'], states)
    gun.dump()

    gun.enable()
    gun.fire()
    gun.hit()
    gun.dump()
    gun.fire()
    gun.hit()
    gun.dump()

    gun.upgrade()
    gun.dump()
    gun.enable()
    gun.fire()
    gun.dump()


