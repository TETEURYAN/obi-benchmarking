import sys
data = sys.stdin.read().split()
N = int(data[0])
G = int(data[1])
M = int(data[2])
total = G * 8 + M * 6
leftover = max(0, total - N)
print(leftover)