import sys

data = sys.stdin.read().split()
if not data:
    exit()
ages = list(map(int, data))
ages.sort()
print(ages[1])