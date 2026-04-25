import sys

data = sys.stdin.read().split()
M = int(data[0])
N = int(data[1])
x = [int(data[i]) for i in range(2, 2 + M)]
y = [int(data[i]) for i in range(2 + M, 2 + M + N)]
max_len = max(M, N)
x_padded = x + [0] * (max_len - M)
y_padded = y + [0] * (max_len - N)
sum_bits = [0] * max_len
carry = 0
for i in range(max_len - 1, -1, -1):
    total = x_padded[i] + y_padded[i] + carry
    sum_bits[i] = total % 2
    carry = total // 2
print(' '.join(map(str, sum_bits)))