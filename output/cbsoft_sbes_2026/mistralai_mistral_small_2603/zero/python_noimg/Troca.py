
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, T = map(int, input[ptr:ptr+2])
    ptr += 2
    top = list(map(int, input[ptr:ptr+N]))
    ptr += N
    bottom = list(map(int, input[ptr:ptr+N]))
    ptr += N

    operations = []
    for _ in range(T):
        I, J = map(int, input[ptr:ptr+2])
        ptr += 2
        operations.append((I-1, J-1))

    flip = [False] * N
    for I, J in operations:
        flip[I] = not flip[I]
        if J + 1 < N:
            flip[J+1] = not flip[J+1]

    current_flip = False
    result = [0] * N
    for i in range(N):
        current_flip ^= flip[i]
        if current_flip:
            result[i] = bottom[i]
        else:
            result[i] = top[i]

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
