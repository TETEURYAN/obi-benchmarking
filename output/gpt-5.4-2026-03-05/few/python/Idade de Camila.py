import sys

ages = list(map(int, sys.stdin.read().split()))
ages.sort()
print(ages[1])