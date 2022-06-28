"""
Generar una matriz ingresando por teclado la cantidad de filas/columnas. Sobre esta primer matriz, realizar la suma de filas y columnas y mostrar una segunda matriz resultante.
"""
import random

# Ask the user for entering the number of rows and columns
ROWS = int(input("Please enter the number of rows you want in the matrix: "))
COLS = int(input("Please enter the number of columns you want in the matrix: "))

matrix = []

# Create the first matrix
for i in range(ROWS):
  matrix.append([])

  for j in range(COLS):
    value = random.randint(1, 10)
    matrix[i].append(value)

# Print the first matrix
print("1) The first matrix:")
for row in matrix:
  for value in row:
    print("\t", value, end=" ")
  print()


# Sum for each row 
for i in range(ROWS):
  accRow = 0
  for j in range(COLS):
    accRow += matrix[i][j]
  print(f"The row number {i + 1} added a total of {accRow}")
  matrix[i].append(accRow) # Append the result as a new element/column

# Sum for each column
for j in range(COLS):
  accCol = 0
  for i in range(ROWS):
    accCol += matrix[i][j]
  print(f"The column number {j + 1} added a total of {accCol}")
  matrix[j].append(accCol) # Append the result as a new element/row

# Print the resultant matrix
print("2) The resultant matrix:")
for row in matrix:
  for value in row:
    print("\t", value, end=" ")
  print()

"""
Explanation: 

1) First we ask the user for entering the number of rows and columns
2) Then, we create the matrix, the same way we did in exercise number 1, with the data the user gave us (rows and cols)
3) Print the matrix
"""


