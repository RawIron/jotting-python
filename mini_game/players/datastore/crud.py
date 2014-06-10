from mongodb import Document, connector


@connector.connect().register
class PlayerIo(Document):
    __database__ = 'playground'
    __collection__ = 'players'
    structure = {'id': int, 'name': unicode}

    @staticmethod
    def factory(init_player):
        p = connector.connect().PlayerIo()
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
        return connector.connect().PlayerIo.factory(init_player)

    def read(self, filter=None):
        if not filter:
            return connector.connect().PlayerIo.find()
        this = filter.where()
        return connector.connect().PlayerIo.find(this)

    def update(self, filter=None):
        pass

    def delete(self, filter=None):
        pass

