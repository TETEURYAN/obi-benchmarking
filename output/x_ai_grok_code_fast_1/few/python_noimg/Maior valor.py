import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
M = int(input_data[1])
S = int(input_data[2])

def sum_digits(x):
    return sum(int(d) for d in str(x))

for i in range(M, N - 1, -1):
    if sum_digits(i) == S:
        print(i)
        sys.exit(0)

print(-1)