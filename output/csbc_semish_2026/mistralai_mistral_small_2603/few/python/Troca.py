
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    T = int(data[ptr])
    ptr += 1

    top = list(map(int, data[ptr:ptr+N]))
    ptr += N
    bottom = list(map(int, data[ptr:ptr+N]))
    ptr += N

    operations = []
    for _ in range(T):
        I = int(data[ptr])
        J = int(data[ptr+1])
        operations.append((I-1, J-1))
        ptr += 2

    flip = [False] * N
    for (I, J) in operations:
        flip[I] = not flip[I]
        if J + 1 < N:
            flip[J+1] = not flip[J+1]

    current_flip = False
    result = []
    for i in range(N):
        current_flip ^= flip[i]
        if current_flip:
            result.append(str(bottom[i]))
        else:
            result.append(str(top[i]))

    print(' '.join(result))

if __name__ == "__main__":
    main()
