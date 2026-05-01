
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
order = [int(x) for x in data[1:]]

position = [0] * (N + 1)
for rank in range(1, N + 1):
    athlete = order[rank - 1]
    position[athlete] = rank

for i in range(1, N + 1):
    print(position[i])
