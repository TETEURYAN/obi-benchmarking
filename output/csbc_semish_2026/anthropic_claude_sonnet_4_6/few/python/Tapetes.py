import sys

def solve():
    data = sys.stdin.read().split()
    L = int(data[0])
    N = int(data[1])
    
    # We need exactly N positive integers that sum to L, maximizing sum of squares.
    # To maximize sum of squares with fixed sum and fixed count of positive integers,
    # we want to make values as unequal as possible: make N-1 of them equal to 1,
    # and one of them equal to L - (N-1).
    # 
    # Proof: given sum S fixed, to maximize sum of squares, concentrate mass.
    # With N values summing to L, minimum each is 1.
    # So set N-1 values to 1 and one value to L-(N-1).
    # 
    # Verify with examples:
    # L=2, N=2: one value = 2-1=1, other=1. Sum of squares = 1+1=2. Correct.
    # L=10, N=5: one value=10-4=6, four values=1. Sum of squares=36+4=40. Correct.
    # L=1000000, N=9: one value=999992, eight values=1. Sum of squares=999992^2+8
    # 999992^2 = (10^6-8)^2 = 10^12 - 16*10^6 + 64 = 999984000064
    # +8 = 999984000072. Correct.
    
    big = L - (N - 1)
    result = big * big + (N - 1)
    print(result)

solve()