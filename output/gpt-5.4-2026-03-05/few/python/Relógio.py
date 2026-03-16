import sys

data = sys.stdin.read().split()
if not data:
    exit()

H = int(data[0])
M = int(data[1])
S = int(data[2])
T = int(data[3])

total = H * 3600 + M * 60 + S
total = (total + T) % (24 * 3600)

h = total // 3600
total %= 3600
m = total // 60
s = total % 60

print(h)
print(m)
print(s)