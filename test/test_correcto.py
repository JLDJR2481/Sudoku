from src.checkSudoku import checkSudoku

def test_correcto():
    assert checkSudoku ([[1,2,3],[2,3,1],[3,1,2]]) == True

def test_correcto2():
    assert checkSudoku([[1, 2, 3],
              [2, 3, 1],
              [2, 3, 1]]) == True