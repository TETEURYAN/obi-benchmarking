import sys

N = int(sys.stdin.read().strip())

if N <= 5:
    left = 'I' * N if N > 0 else '*'
    right = '*'
else:
    left = 'I' * 5
    right = 'I' * (N - 5)

print(left)
print(right)