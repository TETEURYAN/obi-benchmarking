import sys

data = sys.stdin.read().split()
N = int(data[0])
Ri = [int(x) for x in data[1:]]
Ri.sort(reverse=True)
FI = 0
for i in range(1, N + 1):
    if Ri[i - 1] >= i:
        FI = i
    else:
        break
print(FI)