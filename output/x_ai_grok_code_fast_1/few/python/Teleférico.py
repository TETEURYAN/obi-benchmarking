import sys
import math

data = sys.stdin.read().split()
C = int(data[0])
A = int(data[1])

print(math.ceil(A / (C - 1)))