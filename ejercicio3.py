import random

a = 1
b = 50
ROWS = int(input("Enter the number of rows and columns: "))
COLS = ROWS

matrix = []

for i in range(ROWS):
  matrix.append([])
  for j in range(COLS):
    value = random.randint(a, b)
    matrix[i].append(value)

print("This is the matrix: ")
for row in matrix:
  for value in row:
    print("\t", value, end = " ")
  print()

newArr = [] # The array with the elements that form the diagonal
res = 0 # The sum of all newArr's elements

for i in range(ROWS):
  newArr.append(matrix[i][i])
  res += matrix[i][i]


print(f"Diagonal's addition: {res}")
"""
Explanation:

1) We declare two variables, a and b, which define the range for the random number we use for the matrix's values
2) We ask the user for entering the number of rows and columns. This number is the same for both of the variables because if we want to calculate the sum of the diagonal, the matrix must be a square
3) We create te matrix and print it
4) For the main task in this exercise, calculating the sum of the diagonal, we have to iterate the matrix. If we analyze the problem, the elements that we want have an index like this: [0][0], [1][1], [2][2], [3][3], and so on. See? We can get the element using the same value for rows and for columns.
5) Knowing this, we iterate with just one 'For Loop', and in each iteration we get this element: matrix[i][i], where we replicate what we explain before. Once we get the element, we add it to the 'res' variable so we can print it later. 
"""