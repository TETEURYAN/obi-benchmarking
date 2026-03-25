import sys

data = list(map(int, sys.stdin.read().split()))
H, M, S, T = data

total = (H * 3600 + M * 60 + S + T) % 86400
h = total // 3600
total %= 3600
m = total // 60
s = total % 60

print(h)
print(m)
print(s)