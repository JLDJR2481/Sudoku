
def checkFilas(sudoku):

    # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"


    for fila in sudoku:

        for (posicion, numero) in enumerate(fila):
            if numero in fila[posicion + 1:]:
                return False

    return True


