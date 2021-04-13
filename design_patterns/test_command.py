import design_patterns.command as c


def test_gun_is_not_loaded():
    gun = c.Gun()
    assert gun.is_loaded() == False

def test_gun_fires_once_with_one_bullet():
    gun = c.Gun()
    gun.load_with(1)
    gun.fire_it()
    assert gun.is_loaded() == False
