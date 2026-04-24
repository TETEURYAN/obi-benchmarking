import sys

data = sys.stdin.read().split()
if not data:
    exit()

E = int(data[0])
D = int(data[1])

if E > D:
    result = E + D
else:
    result = 2 * (D - E)

print(result)