import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, c, s = data[0], data[1], data[2]
commands = data[3:3 + c]

pos = 1
ans = 1 if pos == s else 0

for x in commands:
    pos += x
    if pos == 0:
        pos = n
    elif pos == n + 1:
        pos = 1
    if pos == s:
        ans += 1

print(ans)