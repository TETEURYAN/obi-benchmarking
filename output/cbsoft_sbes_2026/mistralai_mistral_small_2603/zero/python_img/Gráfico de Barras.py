
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    X = list(map(int, input[ptr:ptr+N]))
    ptr += N

    H = max(X) if max(X) > 0 else 0

    for i in range(H):
        line = []
        for j in range(N):
            if X[j] > i:
                line.append('1')
            else:
                line.append('0')
        print(' '.join(line))

if __name__ == '__main__':
    main()
