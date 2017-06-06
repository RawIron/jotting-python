from path_cd import Path


def test_up_down():
    p = Path('/a/b')
    p.cd('../x')
    assert p.current_path == '/a/x'


def test_absolute():
    p = Path('/a/b')
    p.cd('/x/y')
    assert p.current_path == '/x/y'


def test_absolute_with_up():
    p = Path('/a/b')
    p.cd('/x/../y')
    assert p.current_path == '/y'


def test_absolute_with_up_up():
    p = Path('/a/b')
    p.cd('/x/../../y')
    assert p.current_path == '/y'


def test_up_up_to_root():
    p = Path('/a/b')
    p.cd('../..')
    assert p.current_path == '/'


def test_up_on_root():
    p = Path('/')
    p.cd('..')
    assert p.current_path == '/'


def test_up_up_on_root():
    p = Path('/')
    p.cd('../..')
    assert p.current_path == '/'
