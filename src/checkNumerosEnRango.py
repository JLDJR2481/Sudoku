
def checkNumerosEnRango(sudoku):

    # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"


    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

      for numero in fila:

          if not isinstance(numero, int) or numero not in numerosValidos:
            return False

    return True


