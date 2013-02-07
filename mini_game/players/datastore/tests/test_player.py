
import mock as m
import players.datastore.player as pio


def mock_save_ok():
    mock = m.Mock()
    mock.save.return_value = True
    return mock

with m.patch(pio.Player()) as MockPlayer:
    mock_player = MockPlayer.return_value
    mock_player.create().return_value = {}
    mock_player.all().return_value = {}
    mock_player.save().return_value = True


def test_save_with_method():
    mock = mock_save_ok()
    player = pio.Player(mock)
    rc = player.save()
    assert (rc == True)

def test_save_with_klass():
    player = pio.Player()
    rc = player.save()
    assert (rc == True)


def fetch():
    assert True
