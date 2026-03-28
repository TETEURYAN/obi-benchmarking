import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

if n == 0:
    left = '*'
    right = '*'
elif n <= 5:
    left = 'I' * n
    right = '*'
else:
    left = 'IIIII'
    right = 'I' * (n - 5)

print(left)
print(right)