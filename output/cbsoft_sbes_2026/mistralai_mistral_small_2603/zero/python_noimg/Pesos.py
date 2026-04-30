
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

    left = 0
    right = N - 1
    possible = True

    while left <= right:
        if weights[right] - weights[left] > 8:
            possible = False
            break
        left += 1
        right -= 1

    print('S' if possible else 'N')

if __name__ == '__main__':
    main()
