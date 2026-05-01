import sys
from collections import Counter

data = sys.stdin.read().split()
nums = list(map(int, data))
cnt = Counter(nums)
if max(cnt.values()) <= 4:
    print("S")
else:
    print("N")