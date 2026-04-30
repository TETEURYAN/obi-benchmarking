
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
order = [int(x) for x in data[1:]]

positions = [0] * (N + 1)

for pos in range(1, N + 1):
    athlete = order[pos - 1]
    positions[athlete] = pos

for i in range(1, N + 1):
    print(positions[i])
