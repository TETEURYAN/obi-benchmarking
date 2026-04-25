import sys

data = sys.stdin.read().split()
X = int(data[0])
N = int(data[1])
quota = X
for i in range(N):
    used = int(data[2 + i])
    quota = quota - used + X
print(quota)