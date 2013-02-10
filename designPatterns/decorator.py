#!/usr/bin/env python


class Attacker(object):
    def __init__(self):
        self.strength = 12
    def fire(self):
        return self.strength

class GunArmor(object):
    def __init__(self, gun):
        self.subject = gun
        self.health = 5
    def fire(self):
        self.subject.fire()
    def hit(self, attacker):
        if self.health == 0:
            self.subject.hit(attacker)
        attackerReplace = Attacker()
        if self.health >= attackerReplace.strength:
            self.health -= attackerReplace.fire()
            attackerReplace.strength = 0
        else:
            attackerReplace.strength -= self.health
            self.health = 0
        self.subject.hit(attackerReplace)

class Gun(object):
    def __init__(self):
        self.health = 45
    def fire(self):
        print "fired"
    def hit(self, attacker):
        self.health -= attacker.fire()
        print "hit " + str(self.health)


if __name__ == '__main__':
    attacker = Attacker()
    gun = Gun()
    armor = GunArmor(gun)

    armor.fire()
    armor.hit(attacker)
    armor.hit(attacker)

