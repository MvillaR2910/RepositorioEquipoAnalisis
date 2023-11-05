def celda_vacia(matrix):
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == 0:
                return (row, col)
    return None

def esta_bien(matrix, row, col, num, resultado):
    # Verifica que no se repita el número en la fila
    if num in matrix[row]:
        return False

    # Verifica que no se repita el número en la columna
    if num in [matrix[i][col] for i in range(3)]:
        return False

    # Verifica la suma en la fila y la columna
    row_sum = sum(matrix[row]) + num
    col_sum = sum(matrix[i][col] for i in range(3)) + num
    if row_sum == resultado or col_sum == resultado:
        return True

def resolver_sudoku(matrix, objetivo):
    empty_cell = celda_vacia(matrix)
    if not empty_cell:
        return matrix  # Sudoku resuelto

    row, col = empty_cell

    for num in range(1, 10):
        if esta_bien(matrix, row, col, num, objetivo):
            matrix[row][col] = num

            if resolver_sudoku(matrix, objetivo):
                return matrix

            matrix[row][col] = 0  # Retrocede si no se encuentra una solución válida

    return None  # No se encontró una solución

# Define la matriz del Sudoku con suma objetivo de 14
sudoku1 = [
    [5, 0, 2],
    [8, 5, 0],
    [0, 2, 0]
]

# Define la matriz del Sudoku con suma objetivo de 16
sudoku2 = [
    [3, 6, 7],
    [0, 7, 0],
    [8, 0, 5]
]

resultado1 = resolver_sudoku(sudoku1, 14)
resultado2 = resolver_sudoku(sudoku2, 16)

if resultado1:
    print("Solución del Sudoku 1:")
    for row in resultado1:
        print(row)
else:
    print("No se encontró una solución para el Sudoku 1.")

print()
print("/---/-----/-------/-------/---------/-------/")
print()

if resultado2:
    print("Solución del Sudoku 2:")
    for row in resultado2:
        print(row)
else:
    print("No se encontró una solución para el Sudoku 2.")
