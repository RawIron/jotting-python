import unittest.mock as mock
from players.datastore.player import Player


@mock.patch('mini_game.players.datastore.player.crud.IoCrud')
def test_save_with_method(mock_IoCrud):
    mock_IoCrud.update.return_value = True
    player = Player(mock_IoCrud)
    rc = player.save()
    assert (rc == True)

@mock.patch.object(Player, 'save')
def test_save_with_klass(mock_save):
    mock_save.return_value = True
    player = Player()
    rc = player.save()
    assert (rc == True)


def fetch():
    assert True
