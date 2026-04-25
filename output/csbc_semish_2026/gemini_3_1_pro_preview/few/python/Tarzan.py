import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
D = int(input_data[1])

trees = []
idx = 2
for _ in range(N):
    trees.append((int(input_data[idx]), int(input_data[idx+1])))
    idx += 2

D2 = D * D

visited = [False] * N
visited[0] = True
queue = [0]

count = 1
head = 0

while head < len(queue):
    u = queue[head]
    head += 1
    
    xu, yu = trees[u]
    for v in range(N):
        if not visited[v]:
            xv, yv = trees[v]
            dist2 = (xu - xv) * (xu - xv) + (yu - yv) * (yu - yv)
            if dist2 <= D2:
                visited[v] = True
                queue.append(v)
                count += 1

if count == N:
    print('S')
else:
    print('N')