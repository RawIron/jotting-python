# a small difference in semantics
#   return a generator
#   create a generator

def g_return(a_list):
    """
    when called, this function executes
    all statements before the return
    """
    a_list.reverse()
    return (x for x in range(2))


def g_yield(a_list):
    """
    when called, this function executes
    no statements
    """
    a_list.reverse()
    for x in range(2): yield x


def test_return_generator():
    my_list = [0,1,2,3]
    gen = g_return(my_list)
    assert my_list[0] == 3
    assert gen.next() == 0

def test_yield():
    my_list = [0,1,2,3]
    gen = g_yield(my_list)
    assert my_list[0] == 0
    assert gen.next() == 0
