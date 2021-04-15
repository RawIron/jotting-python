import unittest.mock as mock
import mini_game.players.datastore.player as pio

import mini_game.players
import mini_game.players.player as p


def mock_save_ok():
    mock_player = mock.Mock()
    mock_player.save.return_value = True
    return mock_player

def mock_save_exception():
    mock_player = mock.Mock()
    mock_player.save = mock.Mock(side_effect=Exception('Boom!'))
    return mock_player

def interface_playerio():
    return mock.Mock(spec=pio.Player)


def test_save_ok():
    mock_player = mock_save_ok()
    rc = _save(mock_player)
    assert (rc == True)

def test_save_exception():
    mock_player = mock_save_exception()
    try:
        rc = _save(mock_player)
        assert False
    except Exception as e:
        assert True

def test_save_with_klass():
    with mock.patch("mini_game.players.datastore.player.Player") as MockPlayer:
        mock_player = MockPlayer.return_value
        mock_player.create.return_value = {}
        mock_player.all.return_value = {}
        mock_player.save.return_value = True

        rc = _save(mock_player)
        assert (rc == True)

def test_interface_playerio():
    rc = _save(interface_playerio())


def _save(mock_engine):
    player = p.Player(mock_engine)
    rc = player.save()
    return rc


def fetch():
    assert True
