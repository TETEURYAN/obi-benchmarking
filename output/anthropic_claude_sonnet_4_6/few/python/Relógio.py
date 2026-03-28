import sys

data = sys.stdin.read().split()
H = int(data[0])
M = int(data[1])
S = int(data[2])
T = int(data[3])

total = H * 3600 + M * 60 + S + T
total %= 86400

new_H = total // 3600
total %= 3600
new_M = total // 60
new_S = total % 60

print(new_H)
print(new_M)
print(new_S)