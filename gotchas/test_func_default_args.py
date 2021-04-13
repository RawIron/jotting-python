def f_mutable(a=[]):
    return a

def f_immutable(a=3):
    return a

def test_immutable_arg():
    res = f_immutable()
    res += 2
    assert id(res) != id(f_immutable())

def test_mutable_arg():
    res = f_mutable()
    res.append(1)
    assert id(res) == id(f_mutable())
