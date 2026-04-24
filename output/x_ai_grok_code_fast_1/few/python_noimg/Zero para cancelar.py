import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
nums = [int(x) for x in input_data[1:]]
stack = []
for num in nums:
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)
print(sum(stack))