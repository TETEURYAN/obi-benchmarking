import sys

data = sys.stdin.read().split()
numbers = [int(x) for x in data[:-1]]
max_num = max(numbers)
print(max_num)