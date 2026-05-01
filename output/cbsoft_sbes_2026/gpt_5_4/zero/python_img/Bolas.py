from collections import Counter
import sys

nums = list(map(int, sys.stdin.read().split()))
freq = Counter(nums)
mx = max(freq.values())
n = 8

print("S" if mx <= (n + 1) // 2 else "N")