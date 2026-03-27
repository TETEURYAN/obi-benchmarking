import sys

input_data = sys.stdin.read().split()
L = int(input_data[0])
C = int(input_data[1])

tipo1 = 2 * L * C - L - C + 1
tipo2 = 2 * (L + C) - 4

print(tipo1)
print(tipo2)