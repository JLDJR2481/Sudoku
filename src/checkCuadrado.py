
def checkCuadrado(sudoku):

	# Precondicion
	assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

	sudokuSano = True
	numeroFilas = len(sudoku)

	for fila in sudoku:
		
		if len(fila) != numeroFilas:
			sudokuSano = False
			break

	# Postcondicion
	assert isinstance(sudokuSano, bool), "la interfaz exige devolver un valor lógico"

	return sudokuSano


