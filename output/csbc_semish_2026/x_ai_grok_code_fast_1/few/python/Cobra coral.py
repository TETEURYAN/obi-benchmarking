import sys

nums = list(map(int, sys.stdin.read().split()))
if nums[0] == nums[3]:
    print("F")
else:
    print("V")