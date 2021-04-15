import mini_game.players.datastore.crud as crud


class Player():
    def __init__(self, io_engine=None):
        if io_engine is None:
            self.crud = crud.IoCrud()
        else:
            self.crud = io_engine

    def new(self):
        player = {'id': 4, 'name': u'momo'}
        return self.crud.create(player)

    def all(self):
        players = self.crud.read()
        for player in players:
            print(player)

    def save(self):
        return self.crud.update(self)
