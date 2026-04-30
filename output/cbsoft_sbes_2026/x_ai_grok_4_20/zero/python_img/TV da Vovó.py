
import sys

input = sys.stdin.read
data = input().split()

index = 0
test = 1

while True:
    M = int(data[index])
    N = int(data[index + 1])
    index += 2
    if M == 0 and N == 0:
        break

    image = []
    for i in range(M):
        row = [int(data[index + j]) for j in range(N)]
        image.append(row)
        index += N

    shift_x = 0
    shift_y = 0

    while True:
        X = int(data[index])
        Y = int(data[index + 1])
        index += 2
        if X == 0 and Y == 0:
            break
        shift_x = (shift_x + X) % N
        shift_y = (shift_y + Y) % M

    print(f"Teste {test}")

    for i in range(M):
        for j in range(N):
            orig_i = (i - shift_y) % M
            orig_j = (j - shift_x) % N
            print(image[orig_i][orig_j], end='')
            if j < N - 1:
                print(' ', end='')
            else:
                print()
    print()
    test += 1
