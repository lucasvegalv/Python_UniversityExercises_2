"""
Ingresar valores desde el teclado en una matriz de NxM y mostrar la matriz creada. Ordenar cada una de las filas por el método de selección. Mostrar nuevamente la matriz.
"""

from sqlite3 import Row


ROWS = int(input("Enter the number of rows: "))
COLS = int(input("Enter the number of columns: "))

# Matrix's creation
matrix = []

for i in range(ROWS):
  matrix.append([])
  for j in range(COLS):
    # The user enter the matrix's values
    value = int(input(f"Enter a value for the matrix in the position ({i}, {j}): "))
    matrix[i].append(value)

# Matrix printing
print("a) This is the original matrix: ")
for row in matrix:
  for value in row:
    print("\t", value, end = " ")
  print()

# Selection Sort's Algorithm to order each matrix's row 
row = 0
len = len(matrix[row])
while(row < ROWS):
  for i in range(len - 1):
    for j in range(i + 1, len):
      if(matrix[row][j] < matrix[row][i]):
        matrix[row][j], matrix[row][i] = matrix[row][i], matrix[row][j]  
  row += 1

# Matrix's printing (sorted)
print("b) This is the matrix with every row sorted: ")
for row in matrix:
  for value in row:
    print("\t", value, end = " ")
  print()


"""
Explanation: 

1) The main challenges for this exercise was to sort every row of the matrix using the Selection Sort's Algorithm. For this task, I think about every row as what they are, a simple array! So, the algorithm is the same; we have to sort an array :)
2) To do this, I use an aux variable (row) to indicate the number of the row (array's position in the matrix). This variable starts at 0 and will be adding 1 until we sort every single row. 
3) For doing this, I used a 'While' statement, so we can repeat the main 'operation' for every row. 
4) Inside the 'While', we use the Selection Sort Algorithm! For each row (matrix[row][j]), we apply the algorithm so we can sort them all.
5) Finally, until we start to sort the next row, we have to add 1 to the aux variable  so we can reference the second row, and so on.
6) Once we finished to sort every single row, we print the sorted matrix! We got something like this (example): 

  a) This is the original matrix: 
          37      38      27      5       46 
          32      27      22      17      43 
          36      31      4       20      17 
          1       20      44      8       32 
          39      20      31      4       7 
  
  b) This is the matrix with every row sorted: 
          5       27      37      38      46 
          17      22      27      32      43 
          4       17      20      31      36 
          1       8       20      32      44 
          4       7       20      31      39 
"""