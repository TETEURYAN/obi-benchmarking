
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    N = int(input_data[1])
    
    X = [int(x) for x in input_data[2:2+M]]
    Y = [int(x) for x in input_data[2+M:2+M+N]]
    
    L = max(M, N)
    
    X += [0] * (L - M)
    Y += [0] * (L - N)
    
    result = [0] * L
    carry = 0
    
    for i in range(L - 1, -1, -1):
        total = X[i] + Y[i] + carry
        result[i] = total % 2
        carry = total // 2
        
    while result and result[-1] == 0:
        result.pop()
        
    print(" ".join(map(str, result)))

if __name__ == '__main__':
    main()
