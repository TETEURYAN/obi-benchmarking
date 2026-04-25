import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])
s = int(data[2])

def digit_sum(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total

for i in range(m, n - 1, -1):
    if digit_sum(i) == s:
        print(i)
        break
else:
    print(-1)