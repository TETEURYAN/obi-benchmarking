import sys

S = sys.stdin.read().split()[0]

count = [0] * 26

for c in S:
    count[ord(c) - ord('A')] += 1

print(sum(count))