import sys
data = sys.stdin.read().split()
C = int(data[0])
A = int(data[1])
cap = C - 1
import math
print(math.ceil(A / cap))