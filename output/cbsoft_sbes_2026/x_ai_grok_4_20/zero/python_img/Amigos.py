
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

A = [int(x) for x in data[2:2+N]]
B = [int(x) for x in data[2+N:2+2*N]]

posA = [i for i in range(N) if A[i] == 1]
posB = [i for i in range(N) if B[i] == 1]

def min_moves_to_match(targets, current):
    moves = 0
    for t, c in zip(targets, current):
        moves += abs(t - c)
    return moves

ans = float('inf')

for offset in range(-N, N + 1):
    targets = []
    valid = True
    for i in range(K):
        t = posB[i] + offset
        if t < 0 or t >= N:
            valid = False
            break
        targets.append(t)
    if not valid:
        continue
    moves = min_moves_to_match(targets, posA)
    if moves < ans:
        ans = moves

print(ans)
