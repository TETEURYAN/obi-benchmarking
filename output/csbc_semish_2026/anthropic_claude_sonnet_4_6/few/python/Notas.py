import sys

data = sys.stdin.read().split()
n = int(data[0])
notes = list(map(int, data[1:n+1]))

from collections import Counter
freq = Counter(notes)
max_freq = max(freq.values())
candidates = [k for k, v in freq.items() if v == max_freq]
print(max(candidates))