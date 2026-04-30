
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    weights = list(map(int, input[ptr:ptr+N]))
    ptr += N

    if N == 1:
        print('S')
        return

    max_diff = 8
    possible = True

    for i in range(N - 1):
        if weights[i+1] - weights[i] > max_diff:
            possible = False
            break

    print('S' if possible else 'N')

if __name__ == '__main__':
    main()
