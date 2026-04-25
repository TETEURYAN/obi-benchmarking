import sys

data = sys.stdin.read().split()
n = int(data[0])
stack = []
for i in range(1, n + 1):
    x = int(data[i])
    if x == 0:
        if stack:
            stack.pop()
    else:
        stack.append(x)
print(sum(stack))