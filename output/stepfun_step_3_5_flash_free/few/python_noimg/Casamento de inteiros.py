import sys

data = sys.stdin.read().split()
if not data:
    exit()
A = int(data[0])
B = int(data[1])

sA = str(A)
sB = str(B)
n = max(len(sA), len(sB))
sA = sA.zfill(n)
sB = sB.zfill(n)

keepA = [True] * n
keepB = [True] * n

for i in range(n-1, -1, -1):
    if sA[i] < sB[i]:
        keepA[i] = False
    elif sA[i] > sB[i]:
        keepB[i] = False

ra = ''.join(sA[i] for i in range(n) if keepA[i])
rb = ''.join(sB[i] for i in range(n) if keepB[i])

ra = int(ra) if ra else -1
rb = int(rb) if rb else -1

x, y = sorted([ra, rb])
print(x, y)