import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
order = [int(x) for x in input_data[1:]]
pos = [0] * (N + 1)
for i in range(N):
    atleta = order[i]
    pos[atleta] = i + 1
for i in range(1, N + 1):
    print(pos[i])