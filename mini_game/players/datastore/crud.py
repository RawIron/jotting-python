'''
    this is not working
'''
from mongoengine import Document, StringField, IntField, connect

connect(db='playground')
#  __collection__ = 'players'

class PlayerIo(Document):
    player_id = IntField()
    name = StringField()

    @staticmethod
    def factory(init_player):
        p = PlayerIo()
        for key, value in init_player.iteritems():
            p[key] = value
        p.save()
        return p


class CrudFilter(object):
    def where(self):
        raise NotImplementedError

class SqlFilter(CrudFilter):
    pass
class KeyFilter(CrudFilter):
    pass
class DictFilter(CrudFilter):
    pass


class IoCrud(object):
    def create(self, init_player):
        return PlayerIo.factory(init_player)

    def read(self, filter=None):
        if not filter:
            return PlayerIo.find()
        this = filter.where()
        return PlayerIo.find(this)

    def update(self, filter=None):
        pass

    def delete(self, filter=None):
        pass
