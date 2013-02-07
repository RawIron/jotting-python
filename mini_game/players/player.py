
import datastore.crud as ds


class Player(object):
    def __init__(self, ds):
        self.ds = ds

    def save(self):
        return self.ds.save(self)
