import sys

data = sys.stdin.read().split()
idx = 0
M = int(data[idx]); idx += 1
N = int(data[idx]); idx += 1

X = [int(data[idx+i]) for i in range(M)]; idx += M
Y = [int(data[idx+i]) for i in range(N)]; idx += N

# Pad to same length
L = max(M, N)
X = X + [0] * (L - M)
Y = Y + [0] * (L - N)

# Add from right to left
result = []
carry = 0
for i in range(L-1, -1, -1):
    s = X[i] + Y[i] + carry
    result.append(s % 2)
    carry = s // 2

# carry should be 0 since X+Y < 1
# result is in reverse order
result.reverse()

# Remove trailing zeros (rightmost digit must be 1)
while len(result) > 1 and result[-1] == 0:
    result.pop()

print(*result)