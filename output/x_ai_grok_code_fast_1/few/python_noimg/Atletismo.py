import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
athletes = [int(x) for x in input_data[1:1+N]]
pos = [0] * (N + 1)
for i in range(N):
    athlete = athletes[i]
    pos[athlete] = i + 1
for i in range(1, N + 1):
    print(pos[i])