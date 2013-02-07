
import crud


class Player(object):
    def __init__(self):
        self.crud = crud.IoCrud()

    def new(self):
        player = {'id': 4, 'name': u'momo'}
        return self.crud.create(player)

    def all(self):
        all_players = self.crud.read()
        for player in all_players:
            print player

    def save(self):
        return self.crud.update(self)

