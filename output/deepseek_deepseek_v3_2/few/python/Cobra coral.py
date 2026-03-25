import sys

nums = list(map(int, sys.stdin.read().split()))
if nums[0] == nums[2] and nums[1] == nums[3]:
    print("V")
else:
    print("F")