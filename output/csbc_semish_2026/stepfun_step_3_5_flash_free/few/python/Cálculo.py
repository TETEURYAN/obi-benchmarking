import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    M = int(data[0])
    N = int(data[1])
    X = list(map(int, data[2:2+M]))
    Y = list(map(int, data[2+M:2+M+N]))
    
    L = max(M, N)
    if M < L:
        X += [0] * (L - M)
    if N < L:
        Y += [0] * (L - N)
    
    carry = 0
    result = []
    for i in range(L-1, -1, -1):
        s = X[i] + Y[i] + carry
        result.append(s % 2)
        carry = s // 2
    
    result.reverse()
    while result and result[-1] == 0:
        result.pop()
    
    if result:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()