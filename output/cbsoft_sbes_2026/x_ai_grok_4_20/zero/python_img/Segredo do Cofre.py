
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
bar = list(map(int, data[2:2+N]))
moves = list(map(int, data[2+N:2+N+M]))

count = [0] * 10

prev = 1
for curr in moves:
    if curr > prev:
        for i in range(prev-1, curr):
            count[bar[i]] += 1
    else:
        for i in range(curr-1, prev):
            count[bar[i]] += 1
    prev = curr

print(' '.join(map(str, count)))
