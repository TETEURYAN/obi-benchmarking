
import sys

input = sys.stdin.read
data = input().split()

index = 0
S = int(data[index])
index += 1
T = int(data[index])
index += 1

graph = [[False] * (S + 1) for _ in range(S + 1)]

for _ in range(T):
    X = int(data[index])
    index += 1
    Y = int(data[index])
    index += 1
    graph[X][Y] = True
    graph[Y][X] = True

P = int(data[index])
index += 1

count = 0
for _ in range(P):
    N = int(data[index])
    index += 1
    path = []
    for j in range(N):
        path.append(int(data[index]))
        index += 1
    possible = True
    for i in range(1, N):
        if not graph[path[i-1]][path[i]]:
            possible = False
            break
    if possible:
        count += 1

print(count)
