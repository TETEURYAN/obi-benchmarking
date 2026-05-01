N, M = map(int, input().split())
# This is a Nim-like game. The losing positions are multiples of (M+1).
# If N % (M+1) == 0, the first player (Paula) loses, otherwise Paula wins.
if N % (M + 1) == 0:
    print("Carlos")
else:
    print("Paula")