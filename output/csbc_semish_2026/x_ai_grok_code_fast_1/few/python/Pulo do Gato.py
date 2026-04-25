import sys
from collections import deque

input_data = sys.stdin.read().split()
C = int(input_data[0])
lajotas = list(map(int, input_data[1:]))

dist = [-1] * C
dist[0] = 0
q = deque([0])

while q:
    curr = q.popleft()
    for next_pos in [curr + 1, curr + 2]:
        if next_pos < C and lajotas[next_pos] == 1 and dist[next_pos] == -1:
            dist[next_pos] = dist[curr] + 1
            q.append(next_pos)

print(dist[C - 1])