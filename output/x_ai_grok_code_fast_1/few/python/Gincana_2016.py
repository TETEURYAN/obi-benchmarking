import sys
import math

N, M = map(int, sys.stdin.read().split())
X = M
while X >= 1 and math.gcd(X, N) != 1:
    X -= 1
print(X)