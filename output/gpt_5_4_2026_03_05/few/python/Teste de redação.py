import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n, m = map(int, data[:2])

k = max(n, m // 2)
words = [chr(ord('a') + (i % 26)) for i in range(k)]

print(' '.join(words))