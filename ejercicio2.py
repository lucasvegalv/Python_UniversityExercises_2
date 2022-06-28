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
  matrix[i].append(accRow) # Append the result as a new element/column
COLS += 1 # Update the number of columns

# Sum for each column
newArr = []
for j in range(COLS):
  accCol = 0
  for i in range(ROWS):
    accCol += matrix[i][j]
  newArr.append(accCol) # Append the sum of each column to the new array
matrix.append(newArr) # Append the new array to the matrix

# Print the final and resultant matrix
print("2) The resultant matrix:")
for row in matrix:
  for value in row:
    print("\t", value, end=" ")
  print()

"""
Explanation: 

1) First we ask the user for entering the number of rows and columns
2) Then, we create the matrix, the same way we did in exercise number 1, with the data the user gave us (rows and cols)
3) Print the original matrix
4) In order to add all the elements of the first row array, we iterate through each row, and inside of it we iterate all the elements/columns. In each element's iteration, we add it to the accRow variable.
5) Once we iterate the entire row, we append the result to that row array (creating a new column). Then repeat the same with the next row, then with the next row, and so on.
6) Before we continue, we update the number of columns of our matrix!
7) The last task is to do the same but with columns, so in order to do this we so the same iteration (I use 'j' in the first loop and 'i' in the second one just for the convention that 'j' is for columns and 'i' is for rows). The difference here is that we use the "father"'s index (j) to get


1) The first matrix:
         3       7 
         10      5 
2) The resultant matrix:
         3       7       10 
         10      5       15 
         13      12      25 
"""