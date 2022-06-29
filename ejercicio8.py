"""8) Crear una matriz cuadrada y luego crear una lista que contenga la suma de cada una de las filas de la matriz sin valores repetidos, o sea, dos filas suman igual, el valor debe estar una sola vez en la lista. Mostrar la lista por pantalla la lista ordenada de menor a mayor"""

import random

# Matrix's varibales declaration
FROM = 1 
TO = 10
ROWS = 5
COLS = 5

# Matrix's creation
matrix = []

for i in range(ROWS):
  matrix.append([])
  for j in range(COLS):
    value = random.randint(FROM, TO)
    matrix[i].append(value)

# Matrix's printing
print("1) This is the matrix!")
for row in matrix:
  for value in row:
    print("\t", value, end = " ")
  print()

# Rows' addition
rowsArr = []
for i in range(ROWS):
  accRow = 0
  for j in range(COLS):
    accRow += matrix[i][j]
  
  # Duplicates' validation
  if(accRow not in rowsArr):  
    rowsArr.append(accRow)
  else: 
    print(f"ALERT! {accRow}, the addition of the row number {i + 1}, is already in the list, let's not be repetitive!")

# Printing of the array with all the rows' additions
print(f"2) This is the array with each row's addition: {rowsArr}")

# Sorted array (Selection Sort's algorithm)
len = len(rowsArr)

for i in range(len - 1):
  for j in range(i + 1, len):
    if(rowsArr[j] < rowsArr[i]):
      rowsArr[i], rowsArr[j] = rowsArr[j], rowsArr[i]
print(f"3) This is the sorted array: {rowsArr}")


"""
Explanation: 

1) In this exercise we have to do again some things like matrix's creation, printing and the calculation to reduce (addition) every row. Besides that, the main challenges for this exercise was to create a new array with the rows' additions but not including repeated values. That was the first task!
2) For that, after trying different options, we use just one line of code; with an 'If else' statement, we validate if the row's addition was already in the array we were generating! If that was True, the value was not included in the array.
3) The second challenge was to sort the array. For this, I use the Selection Sort's algorithm.
4) And that's it, here is an example of what we what when we run this program: 

  A) This is the matrix!
          6       5       4       10      8 
          5       4       6       8       5 
          2       8       6       4       6 
          1       5       1       4       5 
          8       1       7       3       10 +

  B) This is the array with each row's addition: [33, 28, 26, 16, 29]

  C) This is the sorted array: [16, 26, 28, 29, 33]
"""