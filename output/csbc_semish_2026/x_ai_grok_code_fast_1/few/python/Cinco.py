import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
D = list(map(int, data[1:]))
candidates = []
for k in range(N - 1):
    if D[k] in [0, 5]:
        newD = D[:]
        newD[k], newD[N - 1] = newD[N - 1], newD[k]
        candidates.append(newD)
if not candidates:
    print(-1)
else:
    best = max(candidates, key=lambda x: ''.join(map(str, x)))
    print(' '.join(map(str, best)))