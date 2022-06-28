import random 

def create_matrix(n, m, a, b):

  matrix = []
  
  if(n <= 0 or m <= 0):
    print("Remember to enter positive numbers for rows and columns!")
    print(f"Sorry, but this is your empty matrix: {matrix}")
  else:
    for i in range(n):
      matrix.append([])
      for j in range(m):
        value = random.randint(a, b)
        matrix[i].append(value)
    
    for row in matrix:
      for value in row:
        print("\t", value, end = " ")
      print()

    rowsArr = []
    for i in range(n):
      accRow = 0
      for j in range(m):
        accRow += matrix[i][j]
      rowsArr.append(accRow)
    print(f"Rows additinon: {rowsArr}")

    colsArr = []
    for j in range(m):
      accCol = 0
      for i in range(n):
        accCol += matrix[i][j]
      colsArr.append(accCol)
    print(f"Columns addition: {colsArr}")

create_matrix(3, 3, 1, 5)

  