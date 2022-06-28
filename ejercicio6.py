""" 6) Desarrollar un programa para crear dos matrices de 3x3 con valores al azar entre dos números ingresados por teclado. Verificar que el rango sea válido, caso contrario solicitar nuevamente ambos valores. Calcular la suma de sus elementos y mostrar la matriz resultante."""

import random

ROWS = 3
COLS = 3

FROM = int(input("Please enter a number to indicate the initial range of the random number: "))
TO = int(input("Please enter a number to indicate the final range of the random number: "))

while(FROM > TO):
  FROM = int(input("Again, please enter a number to indicate the initial range of the random number: "))
  TO = int(input("Now enter a bigger number to indicate the final range of the random number: "))

matrix = []

for i in range(ROWS):
  matrix.append([])
  for j in range(COLS):
    value = random.randint(FROM, TO)
    matrix[i].append(value)

print(f"This is the {ROWS}x{COLS}'s matrix! Its values are from {FROM} to {TO}")
for row in matrix:
  for value in row:
    print("\t", value, end = " ")
  print()