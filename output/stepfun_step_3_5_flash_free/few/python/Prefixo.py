import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
s1 = data[1]
m = int(data[2])
s2 = data[3]

count = 0
min_len = min(n, m)
for i in range(min_len):
    if s1[i] == s2[i]:
        count += 1
    else:
        break

print(count)