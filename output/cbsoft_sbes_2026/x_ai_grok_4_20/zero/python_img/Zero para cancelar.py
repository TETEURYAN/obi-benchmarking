
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
numbers = [int(x) for x in data[1:]]

stack = []
for num in numbers:
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)

print(sum(stack))
