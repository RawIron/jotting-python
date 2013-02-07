#!/usr/bin/python


class Gun(object):
    def fire(self):
        print "fired"

class Target(object):
    def hit(self):
        print "hit" 


class GunFireCommand(object):
    def __init__(self, gun):
        self.receiver = gun
    def execute(self):
        self.receiver.fire()

class TargetHitCommand(object):
    def __init__(self, target):
        self.receiver = target
    def execute(self):
        self.receiver.hit()


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
    command = TargetHitCommand(target)
    server.sent(command)

    server.run()

