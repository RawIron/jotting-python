import mock as m
from mini_game.players.datastore.player import Player


def mock_save_ok():
    mock = m.Mock()
    mock.save.return_value = True
    return mock

with m.patch(Player()) as MockPlayer:
    mock_player = MockPlayer.return_value
    mock_player.create().return_value = {}
    mock_player.all().return_value = {}
    mock_player.save().return_value = True


def test_save_with_method():
    mock = mock_save_ok()
    player = Player(mock)
    rc = player.save()
    assert (rc == True)

def test_save_with_klass():
    player = Player()
    rc = player.save()
    assert (rc == True)


def fetch():
    assert True
