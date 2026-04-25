import sys

data = sys.stdin.read().split()
n = int(data[0])
total = 0
days = 0
for i in range(1, n + 1):
    total += int(data[i])
    days += 1
    if total >= 1000000:
        break
print(days)