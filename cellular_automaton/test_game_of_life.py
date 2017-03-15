import game_of_life as matrix


def test_dim():
    m = matrix.init_matrix(3, 4)
    assert matrix.dim_matrix(m) == (4,3)


def test_flatten():
    m = [[2,3], [4,6]]
    assert matrix.flatten_matrix(m) == [2,3,4,6]


def test_extract():
    m = [range(0,5), range(5,10), range(10,15)]
    sub_matrix = [[5,6,7], [10,11,12], [0,1,2]]
    assert matrix.extract_matrix(m, 2, 1, 1) == sub_matrix
    
