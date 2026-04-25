
def solve():
    line1 = input().split()
    M, N = int(line1[0]), int(line1[1])
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    max_len = max(M, N)
    
    # Pad both to same length
    X_padded = X + [0] * (max_len - M)
    Y_padded = Y + [0] * (max_len - N)
    
    # Add from right to left
    result = []
    carry = 0
    for i in range(max_len - 1, -1, -1):
        s = X_padded[i] + Y_padded[i] + carry
        result.append(s % 2)
        carry = s // 2
    
    # If carry remains, prepend (but problem says X+Y < 1, so carry at position 0 means integer part)
    # Actually carry here would mean the sum >= 1, but constraints say X+Y < 1
    # Still handle it just in case
    if carry:
        result.append(carry)
    
    result.reverse()
    
    # Remove trailing zeros (obi-2015 uses minimum digits, last digit must be 1)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    print(' '.join(map(str, result)))

solve()
