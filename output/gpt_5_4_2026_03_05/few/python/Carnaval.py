import sys

vals = list(map(float, sys.stdin.read().split()))
total = sum(vals) - min(vals) - max(vals)
print(f"{total:.1f}")