from path_cd import Path, PathString


def _create_path():
    return Path


def test_up_down():
    p = _create_path()('/a/b')
    p.cd('../x')
    assert p.current_path == '/a/x'


def test_absolute():
    p = _create_path()('/a/b')
    p.cd('/x/y')
    assert p.current_path == '/x/y'


def test_absolute_with_up():
    p = _create_path()('/a/b')
    p.cd('/x/../y')
    assert p.current_path == '/y'


def test_absolute_with_up_up():
    p = _create_path()('/a/b')
    p.cd('/x/../../y')
    assert p.current_path == '/y'


def test_up_up_to_root():
    p = _create_path()('/a/b')
    p.cd('../..')
    assert p.current_path == '/'


def test_up_on_root():
    p = _create_path()('/')
    p.cd('..')
    assert p.current_path == '/'


def test_up_up_on_root():
    p = _create_path()('/')
    p.cd('../..')
    assert p.current_path == '/'
