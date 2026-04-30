
import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
X = int(data[3])
Y = int(data[4])
Z = int(data[5])

if C > Z:
    print(0)
    sys.exit()

max_cont = 0

# Orientação 1: A -> X, B -> Y
if A <= X and B <= Y:
    nx = X // A
    ny = Y // B
    max_cont = max(max_cont, nx * ny)

# Orientação 2: B -> X, A -> Y
if B <= X and A <= Y:
    nx = X // B
    ny = Y // A
    max_cont = max(max_cont, nx * ny)

print(max_cont)
