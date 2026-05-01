import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    digits = list(map(int, input_data[1:n+1]))
    
    # We need to swap two positions to make the last digit 0 or 5
    # The number is divisible by 5 if last digit is 0 or 5
    # Current last digit is not 0 or 5 (number not divisible by 5)
    
    best = None
    
    # Try all possible swaps
    for i in range(n):
        for j in range(i+1, n):
            new_digits = digits[:]
            new_digits[i], new_digits[j] = new_digits[j], new_digits[i]
            # Check if divisible by 5
            if new_digits[-1] == 0 or new_digits[-1] == 5:
                # Check leading zero
                if new_digits[0] == 0 and n > 1:
                    continue
                if best is None or new_digits > best:
                    best = new_digits
    
    if best is None:
        print(-1)
    else:
        print(*best)

solve()