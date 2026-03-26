import sys

data = sys.stdin.read().split()
n = int(data[0])
p = data[1]
m = int(data[2])
s = data[3]

count = 0
for i in range(min(n, m)):
    if p[i] == s[i]:
        count += 1
    else:
        break

print(count)