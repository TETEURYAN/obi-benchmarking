
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    M = int(data[idx])
    N = int(data[idx + 1])
    idx += 2
    X = list(map(int, data[idx:idx + M]))
    idx += M
    Y = list(map(int, data[idx:idx + N]))

    carry = 0
    result = []
    i = M - 1
    j = N - 1
    pos = 0

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += X[i]
            i -= 1
        if j >= 0:
            total += Y[j]
            j -= 1
        carry = total // 2
        result.append(total % 2)
        pos += 1

    result.reverse()
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
