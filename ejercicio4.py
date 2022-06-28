import random

ROWS = 4
COLS = 3

matrix = []

for i in range(ROWS):
  matrix.append([])
  for j in range(COLS):
    value = random.randint(1, 50)
    matrix[i].append(value)

for row in matrix:
  for value in row:
    print("\t", value, end = " ")
  print()

max = matrix[0][0]
posRow = 0
posCol = 0
print(f"The max is: {max}")
for i in range(ROWS):
  for j in range(COLS):
    if(matrix[i][j] > max):
      max = matrix[i][j]
      posRow = i
      posCol = j
      print(f"The new max is: {max} in the position: Row {posRow + 1}, Column {posCol + 1}.")
print(f"The final max of the matrix is: {max} in the position: Row {posRow + 1}, Column {posCol + 1}.")

"""
Explanation:

1) Let's skip the creation of the matrix's part because we have been doing and explaining that in previous exercises
2) Once we have our matrix, we want to get the max value of it. How do we do it? Iterating the same way as we do when we fill a matrix; Each row, and inside each row getting each element/column.
3) Knowing this, we do that iteration (line 25). But before we start iterating the matrix, we declare three fundamental variables; the max, and other two variables to store the position of it. We use the max variable so we have a value to compare with, in this case we use the first element of the matrix, so until there are a bigger value...  That's the max!
4) In the iteration, we do the main operation: compare. We compare the current value with the max, and if it's True, the current value is the new max. Also, we store the positions' values so we can inform where is the max
5) Finally, we print what we got!
"""