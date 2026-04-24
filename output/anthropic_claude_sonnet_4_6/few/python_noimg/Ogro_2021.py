import sys
n = int(sys.stdin.read().strip())
left = min(n, 5)
right = max(0, n - 5)
print('I' * left if left > 0 else '*')
print('I' * right if right > 0 else '*')