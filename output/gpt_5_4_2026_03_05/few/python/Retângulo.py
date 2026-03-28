import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
L = data[1:1+n]

total = sum(L)
if total % 2 != 0:
    print('N')
    sys.exit()

half = total // 2

pos = 0
seen = set()
for x in L:
    seen.add(pos)
    pos += x

for p in seen:
    if (p + half) in seen:
        print('S')
        sys.exit()

print('N')