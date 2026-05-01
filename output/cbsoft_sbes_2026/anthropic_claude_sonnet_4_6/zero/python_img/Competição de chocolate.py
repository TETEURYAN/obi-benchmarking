N, M = map(int, input().split())

# This is a Nim-like game. The key insight:
# If N % (M+1) == 0, the current player (Paula) loses, otherwise Paula wins.
# This is because:
# - If remaining = 0, current player already lost (previous player took last)
# - If remaining % (M+1) == 0, current player loses (any move 1..M leaves opponent in winning position)
# - Otherwise, current player wins by taking N % (M+1) chocolates

if N % (M + 1) == 0:
    print("Carlos")
else:
    print("Paula")