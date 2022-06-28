import random

matrix = []

for i in range(3):
  matrix.append([])

  for j in range(4):
    value = random.randint(1, 10)
    matrix[i].append(value)

print("Esta es la matriz:")
print("------------------------")
for row in matrix:
  for value in row:
      print("\t", value, end=" ")
  print()

"""Explanation
1) Declaraion of an empty array, the 'extern' one
2) With a 'For Loop', we iterate the number of rows (3)
3) For each iteration (in each row) we append an empty array ready to be filled with elements (columns)
4) Then, with another 'For Loop', we iterate the number of columns (4)
5) Each iteration, each column of the current row, we append a random value
6) This way we will go to the first row, and append a random number as many times as we define in the 'j' iteration
7) Once we fill the entire row with its columns, we go to the second row and repeat the same. How many times? As many as you define in the first iteration (number of rows)
8) Once we have our matrix, we wanna show it! For doing this we will make a similar iteration; for each row we iterate all the columns' values and print each of them between empty spaces so it looks better :)
9) The '/t' is for a faster alignment, and the 'end=  ' is for not jumping to a new line after each value's print
10) In conclusion we'll get something like this, a 3x4 matrix (remember the values are random):
  
  This is the matrix:
          8       6       6       6 
          10      6       7       1 
          3       9       5       10 

"""