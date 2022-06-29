import random

COLS = 4
ROWS = int(input("Enter a number: "))
while(ROWS % 4 != 0):
  ROWS = int(input("Please enter a multiple of 4's number: "))
  
matrix = []

for i in range(ROWS):
  matrix.append([])
  for j in range(COLS):
    value = random.randint(1, 50)
    matrix[i].append(value)

print(f"This is your {ROWS}x{COLS}'s matrix!")
for rows in matrix:
  for values in rows:
    print("\t", values, end = " ")
  print()    

""" 
Explanation: 

1) Honestly, I'm not sure if what I did is what the instruction asks for :) But the challenge here is to build the matrix with a user's input and validate that its input is multiple of 4.
"""