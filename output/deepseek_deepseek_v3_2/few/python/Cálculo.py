import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    M = int(data[0])
    N = int(data[1])
    X = data[2:2 + M]
    Y = data[2 + M:2 + M + N]
    
    # Build the binary strings from input lists
    x_bin = ''.join(X)
    y_bin = ''.join(Y)
    
    # Convert to decimal value using the given weighting (2^(-i))
    x_val = 0.0
    for i, bit in enumerate(x_bin):
        if bit == '1':
            x_val += 2**(-(i + 1))
    
    y_val = 0.0
    for i, bit in enumerate(y_bin):
        if bit == '1':
            y_val += 2**(-(i + 1))
    
    total = x_val + y_val
    
    # Convert total to obi‑2015 representation
    result = []
    i = 1
    while total > 0:
        if total >= 2**(-i):
            result.append('1')
            total -= 2**(-i)
        else:
            result.append('0')
        i += 1
    # Ensure last digit is 1 (minimal representation)
    if result[-1] == '0':
        result[-1] = '1'
    
    print(' '.join(result))

if __name__ == "__main__":
    main()