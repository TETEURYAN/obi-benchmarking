from collections import Counter
import sys

nums = list(map(int, sys.stdin.read().split()))
freq = Counter(nums)
mx = max(freq.values())

print("S" if mx <= (len(nums) + 1) // 2 else "N")