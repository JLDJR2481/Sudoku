from src.checkSudoku import checkSudoku


def test_incorrecto1():
    assert checkSudoku([[1, 2, 3, 4],
                        [2, 3, 1, 3],
                        [3, 1, 2, 3],
                        [4, 4, 4, 2]]) == False


def test_incorrecto2():
    assert checkSudoku([[1, 2, 3, 4],
                        [2, 3, 1, 2],
                        [4, 1, 2, 3],
                        [2, 3, 1, 4]]) == False


def test_incorrecto3():
    assert checkSudoku([[1, 2, 3, 4, 5],
                        [2, 3, 1, 5, 6],
                        [4, 5, 2, 1, 3],
                        [3, 4, 5, 2, 1],
                        [5, 6, 4, 3, 2]]) == False


def test_incorrecto4():
    assert checkSudoku([['a', 'b', 'c'],
                        ['b', 'c', 'a'],
                        ['c', 'a', 'b']]) == False


def test_incorrecto5():
    assert checkSudoku([[1, 1.5],
                        [1.5, 1]]) == False


def test_regular():
    assert checkSudoku([[1, 2, 3],
                        [2, 3, 1]]) == False


def test_regular2():
    assert checkSudoku([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1]]) == False
