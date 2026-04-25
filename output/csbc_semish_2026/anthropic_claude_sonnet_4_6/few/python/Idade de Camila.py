import sys
ages = list(map(int, sys.stdin.read().split()))
print(sorted(ages)[1])