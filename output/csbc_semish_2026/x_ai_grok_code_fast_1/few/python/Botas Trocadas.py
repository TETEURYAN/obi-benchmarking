import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])

left = [0] * 61

right = [0] * 61

idx = 1

for i in range(N):

    M = int(input_data[idx])

    L = input_data[idx + 1]

    if L == 'E':

        left[M] += 1

    else:

        right[M] += 1

    idx += 2

pairs = 0

for m in range(30, 61):

    pairs += min(left[m], right[m])

print(pairs)