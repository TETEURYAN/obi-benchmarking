import sys

data = sys.stdin.read().split()
n = int(data[0])
values = list(map(int, data[1:n+1]))

max_count = 1
current = 1
for i in range(1, n):
    if values[i] == values[i-1]:
        current += 1
        if current > max_count:
            max_count = current
    else:
        current = 1

print(max_count)