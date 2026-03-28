import sys

data = sys.stdin.read().split()
n = int(data[0])
r = [int(data[i+1]) for i in range(n)]
r.sort(reverse=True)
fi = 0
for i, val in enumerate(r):
    if val >= i + 1:
        fi = i + 1
    else:
        break
print(fi)