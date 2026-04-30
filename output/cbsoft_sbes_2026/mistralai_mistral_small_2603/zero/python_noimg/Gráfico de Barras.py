
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    X = list(map(int, input[ptr:ptr+N]))
    ptr += N

    H = max(X) if X else 0

    for h in range(H):
        line = []
        for xi in X:
            if h < (H - xi):
                line.append('0')
            else:
                line.append('1')
        print(' '.join(line))

if __name__ == "__main__":
    main()
