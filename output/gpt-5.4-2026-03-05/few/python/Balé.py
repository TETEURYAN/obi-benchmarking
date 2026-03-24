import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1 + n]

stack = []
ans = 0

for x in a:
    while stack and stack[-1] < x:
        stack.pop()
    ans += len(stack)
    stack.append(x)

print(ans)