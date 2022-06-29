import random 

def create_matrix(n, m, a, b):

  matrix = []
  
  # Range validation
  if(n <= 0 or m <= 0): 
    print("Remember to enter positive numbers for rows and columns!")
    print(f"Sorry, but this is your empty matrix: {matrix}")
  else:
    # Matrix's creation
    for i in range(n):
      matrix.append([])
      for j in range(m):
        value = random.randint(a, b)
        matrix[i].append(value)
    
    # Matrix's printing
    for row in matrix:
      for value in row:
        print("\t", value, end = " ")
      print()

    # Rows' addition
    rowsArr = []
    for i in range(n):
      accRow = 0
      for j in range(m):
        accRow += matrix[i][j]
      rowsArr.append(accRow)
    print(f"Rows additinon: {rowsArr}")

    # Columns' addition
    colsArr = []
    for j in range(m):
      accCol = 0
      for i in range(n):
        accCol += matrix[i][j]
      colsArr.append(accCol)
    print(f"Columns addition: {colsArr}")

create_matrix(3, 3, 1, 5)

"""
Explanation: 

1) The main challenge for this exercise was to validate the row and column's values
2) In order to do this, inside the function we use an 'If else' statement. If the values are invalid, we end the program printing the empty matrix. If the values are valid (graters than 0), we continue with the program (creating the matrix, printing it and calculating some additions)
"""