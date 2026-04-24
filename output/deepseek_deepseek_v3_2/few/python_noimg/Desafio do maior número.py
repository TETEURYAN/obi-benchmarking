import sys

data = sys.stdin.read().split()
max_val = 0
for token in data:
    num = int(token)
    if num == 0:
        break
    if num > max_val:
        max_val = num
print(max_val)