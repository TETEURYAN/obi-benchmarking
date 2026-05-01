
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    A = list(map(int, input[ptr:ptr+N]))

    is_escher = True
    for i in range(N // 2):
        if A[i] + A[N - 1 - i] != A[i + 1] + A[N - 2 - i]:
            is_escher = False
            break

    print('S' if is_escher else 'N')

if __name__ == '__main__':
    main()
