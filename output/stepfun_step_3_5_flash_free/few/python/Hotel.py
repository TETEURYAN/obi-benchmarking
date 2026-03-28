import sys
D, A, N = map(int, sys.stdin.read().split())
print((32 - N) * (D + min(N - 1, 14) * A))