from src.checkCuadrado      import checkCuadrado
from src.checkNumerosEnRango import checkNumerosEnRango
from src.checkFilas         import checkFilas
from src.checkColumnas      import checkColumnas

def checkSudoku(sudoku):

    # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"
    
    sudokuSano = checkCuadrado(sudoku) and checkNumerosEnRango(sudoku) and checkFilas(sudoku) and checkColumnas(sudoku)

    # Postcondicion
    assert isinstance(sudokuSano, bool)

    return sudokuSano

    