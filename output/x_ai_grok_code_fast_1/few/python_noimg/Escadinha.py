import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
a = list(map(int, input_data[1:]))

if N == 1:
    print(1)
else:
    count = 1
    for i in range(2, N):
        if a[i] - a[i-1] != a[i-1] - a[i-2]:
            count += 1
    print(count)