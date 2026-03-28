import sys
nums = list(map(int, sys.stdin.read().split()))
print(max(x for x in nums if x != 0))