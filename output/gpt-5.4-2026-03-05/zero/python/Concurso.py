import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

N, K = data[0], data[1]
A = data[2:2 + N]

A.sort(reverse=True)
print(A[K - 1] if K > 0 else max(A))