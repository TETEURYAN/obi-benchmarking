import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
a = 0
b = 0

for i in range(1, n + 1):
    if data[i] == '1':
        a ^= 1
    else:
        a ^= 1
        b ^= 1

print(a)
print(b)