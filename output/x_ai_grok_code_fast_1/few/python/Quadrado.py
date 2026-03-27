import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
if N == 1:
    print(1)
elif N == 2:
    print(-1)
elif N == 3:
    print(1, 2, 3)
    print(4, 5, 6)
    print(7, 8, 9)
elif N == 4:
    print(1, 2, 3, 6)
    print(7, 8, 9, 12)
    print(13, 14, 15, 18)
    print(31, 32, 33, 36)
elif N % 2 == 0:
    print(-1)
else:
    for i in range(N):
        row = [i * N + j + 1 for j in range(N)]
        print(*row)