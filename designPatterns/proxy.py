#!/usr/bin/python


class CachedInventoryProxy(object):
    def __init__(self, proxied):
        self.subject = proxied
        self.cache = []
    def load(self):
        if not self.subject.isLoaded:
            self.subject.load()
            self.cache = self.subject
        else:
            print "read from cache"
    def save(self):
        print "save to cache"
    def add(self, gun):
        self.subject.add(gun)
    def remove(self, gun):
        self.subject.remove(gun)


class GunsInventory(object):
    def __init__(self):
        self.inventory = []
        self.isLoaded = False
        self.isDirty = False
    def load(self):
        print "read from db"
        self.isLoaded = True
    def save(self):
        if isDirty:
            print "save to db"
            self.isDirty = False
    def add(self, gun):
        if isLoaded:
            inventory.add(gun)
            self.isDirty = True
    def remove(self, gun):
        if isLoaded:
            inventory.remove(gun)
            self.isDirty = True



if __name__ == '__main__':
    guns = GunsInventory()
    proxy = CachedInventoryProxy(guns)
    proxy.load()
    proxy.load()
    proxy.save()
    proxy.load()
