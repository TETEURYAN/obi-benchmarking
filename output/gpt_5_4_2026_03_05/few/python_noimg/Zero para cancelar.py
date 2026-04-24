import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
stack = []
total = 0

for x in data[1:n+1]:
    if x == 0:
        if stack:
            total -= stack.pop()
    else:
        stack.append(x)
        total += x

print(total)