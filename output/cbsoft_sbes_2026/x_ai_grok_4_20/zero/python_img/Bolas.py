
from collections import Counter
import sys

input = sys.stdin.read
data = input().strip().split()
balls = list(map(int, data))

if len(balls) != 8:
    balls = balls[:8]

freq = Counter(balls)
max_count = max(freq.values())

if max_count > 4:
    print("N")
else:
    print("S")
