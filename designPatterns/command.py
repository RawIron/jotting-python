#!/usr/bin/env python


class Gun(object):
    def __init__(self):
        self.bullets = 0
        self.firerate = 1
        self.force = 3
    def load_with(self, bullets):
        self.bullets += bullets
    def is_loaded(self):
        return (self.bullets > 0)
    def fire_it(self):
        fired = min(self.bullets, self.firerate)
        self.bullets = max(0, self.bullets - self.firerate)
        return self

class Target(object):
    def __init__(self):
        self.health = 5
    def got_hit_with(self, force):
        self.health = max(0, self.health - force)
    def is_destroyed(self):
        return (self.health == 0)


class GunFireCommand(object):
    def __init__(self, gun):
        self.receiver = gun
    def execute(self):
        self.receiver.fire_it()

class TargetHitCommand(object):
    def __init__(self, target, with_force):
        self.receiver = target
        self.force = with_force
    def execute(self):
        self.receiver.got_hit_with(self.force)


class Server(object):
    def __init__(self):
        self.commands = []
    def sent(self, command):
        self.commands.append(command)
    def run(self):
        for command in self.commands:
            command.execute()


if __name__ == '__main__':
    gun = Gun()
    target = Target()
    server = Server()

    command = GunFireCommand(gun)
    server.sent(command)
    server.sent(command)
    command = TargetHitCommand(target, 3)
    server.sent(command)

    server.run()

