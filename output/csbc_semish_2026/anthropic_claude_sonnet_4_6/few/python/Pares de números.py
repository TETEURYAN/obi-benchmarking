import sys

data = sys.stdin.read().split()
n = int(data[0])
I = int(data[1])
F = int(data[2])
v = [int(data[i+3]) for i in range(n)]

count = 0
for i in range(n):
    for j in range(i+1, n):
        s = v[i] + v[j]
        if I <= s <= F:
            count += 1

print(count)