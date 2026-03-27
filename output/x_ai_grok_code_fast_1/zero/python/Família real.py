
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
parents = [0] + [int(x) for x in data[2:2+N]]
attended = set(int(x) for x in data[2+N:])

children = [[] for _ in range(N+1)]
for i in range(1, N+1):
    children[parents[i]].append(i)

generation = [-1] * (N+1)
generation[0] = 0
q = deque([0])
while q:
    curr = q.popleft()
    for child in children[curr]:
        if generation[child] == -1:
            generation[child] = generation[curr] + 1
            q.append(child)

max_gen = max(generation[1:]) if N > 0 else 0
result = []
for gen in range(1, max_gen+1):
    total = sum(1 for i in range(1, N+1) if generation[i] == gen)
    attended_count = sum(1 for i in range(1, N+1) if generation[i] == gen and i in attended)
    perc = (attended_count / total * 100) if total > 0 else 0.0
    result.append(f"{perc:.2f}")
print(" ".join(result))
