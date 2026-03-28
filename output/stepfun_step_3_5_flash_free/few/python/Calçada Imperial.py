import sys
from collections import defaultdict

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
seq = list(map(int, data[1:1+n]))

pos = defaultdict(list)
for i, v in enumerate(seq):
    pos[v].append(i)

vals = list(pos.keys())
ans = 1

for i in range(len(vals)):
    for j in range(i+1, len(vals)):
        a, b = vals[i], vals[j]
        A, B = pos[a], pos[b]
        pA = pB = 0
        last = None
        cnt = 0
        while pA < len(A) or pB < len(B):
            if pA < len(A) and (pB >= len(B) or A[pA] < B[pB]):
                val = a
                pA += 1
            else:
                val = b
                pB += 1
            if val != last:
                cnt += 1
                last = val
        if cnt > ans:
            ans = cnt

print(ans)